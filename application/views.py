from flask import render_template, request, redirect, url_for
from application import app

from crontab import CronTab
from .forms import CronForm, UserForm, RawForm


@app.route('/', methods=['GET', 'POST'])
def main():
    form = UserForm(request.form)
    if request.method == "POST" and form.validate():
        return redirect(url_for("cron_list", username=form.account.data))
    return render_template("main.html", form=form)


@app.route('/cron_add/<username>', methods=['GET', 'POST'])
def cron_add(username, minutes=0, hour=0):
    form = CronForm(request.form)
    if request.method =="POST" and form.validate():
        if form.minutes.data:
            minutes=form.minutes.data
        if form.hour.data:
            hour=form.hour.data
        my_cron = CronTab(user=form.account.data)
        job = my_cron.new(command=form.executable.data)
        if form.type.data == "horly":
            job.minutes.on(minutes)
        elif form.type.data == "daily":
            job.hour.on(hour)
            job.minutes.on(minutes)
        elif form.type.data == "weekly":
            job.hour.on(hour)
            job.minutes.on(minutes)
            job.dow.on(1)
        elif form.type.data == "monthly":
            job.hour.on(hour)
            job.minutes.on(minutes)
            job.day.on(1)
            job.month.during(1, 12)
        my_cron.write()
        return redirect(url_for("cron_list", username=username))

    return render_template('cron_add.html', form=form, username=username)


@app.route('/cron_raw/<username>', methods=['GET', 'POST'])
def cron_raw(username):
    form = RawForm(request.form)
    if request.method == "POST" and form.validate():
        my_cron = CronTab(user=username)
        job = my_cron.new(command=form.executable.data)
        job.setall(form.raw.data)
        my_cron.write()
        return redirect(url_for("cron_list", username=username))
    return render_template("cron_raw.html", form=form, username=username)


@app.route('/list/<username>')
def cron_list(username):
    my_cron = CronTab(user=username)
    return render_template('cron_list.html', jobs=my_cron, username=username)


@app.route('/edit', methods=['GET', 'POST'])
def cron_edit():
    return ""
