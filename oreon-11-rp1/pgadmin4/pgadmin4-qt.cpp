/*************************************************************************
*
* Copyright (C) 2021 Sandro Mani <manisandro@gmail.com>
* This software is released under the PostgreSQL Licence
*
*************************************************************************/

/* Qt WebEngineView widget to display pgAdmin4 as a desktop application */

#include <QApplication>
#include <QDesktopServices>
#include <QEventLoop>
#include <QFileDialog>
#include <QIcon>
#include <QMessageBox>
#include <QProcess>
#include <QSplashScreen>
#include <QTcpSocket>
#include <QTextStream>
#include <QTimer>
#include <QUuid>
#include <QWebEngineDownloadRequest>
#include <QWebEngineProfile>
#include <QWebEngineSettings>
#include <QWebEngineView>



class WebEnginePage : public QWebEnginePage {

    using QWebEnginePage::QWebEnginePage;

public:
    bool acceptNavigationRequest(const QUrl &url, QWebEnginePage::NavigationType type, bool isMainFrame) override {
        if (type == QWebEnginePage::NavigationTypeLinkClicked)
        {
                QDesktopServices::openUrl(url);
                return false;
        }
        return QWebEnginePage::acceptNavigationRequest(url, type, isMainFrame);
    }
};


class WebEngineView : public QWebEngineView {

    using QWebEngineView::QWebEngineView;

public:
    WebEngineView(const QString& url) {
        WebEnginePage* page = new WebEnginePage(&mExternalLinkView);
        page->profile()->queryPermission(url, QWebEnginePermission::PermissionType::ClipboardReadWrite).grant();
        connect(page->profile(), &QWebEngineProfile::downloadRequested, this, &WebEngineView::downloadRequested);
        mExternalLinkView.setPage(page);
    }

protected:
    QWebEngineView* createWindow(QWebEnginePage::WebWindowType type) override {
        return &mExternalLinkView;
    }

private:
    QWebEngineView mExternalLinkView;

    void downloadRequested(QWebEngineDownloadRequest* download) {
        QString filename = QFileDialog::getSaveFileName(this, "Save File", download->suggestedFileName());
        if (!filename.isEmpty()) {
            download->setDownloadFileName(filename);
            download->accept();
        }
    }
};


int main(int argc, char* argv[]) {
    QApplication app(argc, argv);
    app.setDesktopFileName("pgadmin4");

    QTextStream qout(stdout);
    QTextStream qerr(stderr);

    // Show splash screen
    QPixmap pixmap("/usr/share/pgadmin4-qt/pgadmin4-qt.svg");
    QSplashScreen splash(pixmap);
    splash.show();

    // Find a free port
    QTcpSocket socket;
    socket.bind();
    int port = socket.localPort();
    socket.close();

    // Run pgadmin4
    QString uuid = QUuid::createUuid().toString(QUuid::WithoutBraces);
    QProcess process;
    QProcessEnvironment env = QProcessEnvironment::systemEnvironment();
    env.insert("PGADMIN_INT_PORT", QString::number(port));
    env.insert("PGADMIN_SERVER_MODE", QString("OFF"));
    process.setProcessEnvironment(env);
    process.start("/usr/bin/python3", {"/usr/lib/pgadmin4/pgAdmin4.py"});
    QObject::connect(&process, &QProcess::readyReadStandardOutput, [&]{
        qout << process.readAllStandardOutput();
        qout.flush();
    });
    QObject::connect(&process, &QProcess::readyReadStandardError, [&]{
        qerr << process.readAllStandardError();
        qerr.flush();
    });

    // Wait for process
    QTcpSocket connectionSocket;
    QTimer timer;
    QEventLoop loop;
    QObject::connect(&timer, &QTimer::timeout, &loop, &QEventLoop::quit);
    for(int i = 0; i < 20; ++i) {
        connectionSocket.connectToHost("127.0.0.1", port);
        connectionSocket.waitForConnected(5000);

        if (connectionSocket.state() == QTcpSocket::ConnectedState) {
            break;
        }
        timer.start(1000);
        loop.exec();
    }

    if (connectionSocket.state() == QTcpSocket::UnconnectedState) {
        QMessageBox::warning(nullptr, "pgAdmin4", "Failed to launch pgAdmin4. Please launch pgadmin4-qt from the command line to get the detailed error output and submit a bug report at <a href=\"https://bugzilla.redhat.com\">https://bugzilla.redhat.com</a>.");
        process.terminate();
        process.waitForFinished();
        return 1;
    }

    connectionSocket.close();

    QString url = QString("http://localhost:%1?key=%2").arg(port).arg(uuid);
    WebEngineView view(url);
    view.settings()->setAttribute(QWebEngineSettings::JavascriptCanOpenWindows, true);
    view.settings()->setAttribute(QWebEngineSettings::JavascriptCanAccessClipboard, true);
    view.setWindowIcon(QIcon("/usr/share/icons/hicolor/128x128/apps/pgadmin4.png"));
    view.setWindowTitle("pgAdmin4-qt - Unofficial runtime for pgadmin4");
    view.resize(1024, 768);
    view.load(url);
    view.showMaximized();
    splash.finish(&view);

    QMessageBox::information(&view, "pgAdmin4-qt", "This is an unofficial runtime for pgAdmin4, developed specifically to ease packaging for Fedora. Some features might be missing compared to the official runtime. When using this runtime, please submit any issues to the Fedora bugtracker at <a href=\"https://bugzilla.redhat.com\">https://bugzilla.redhat.com</a>. There is no upstream support for this runtime.");

    int result = app.exec();

    process.terminate();
    process.waitForFinished();

    return result;
}
