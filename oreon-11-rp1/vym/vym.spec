%global source0_hash 69dc9780e3fed0d44ca964cfdae909b08c7e1df8804d499401bedf4112e5eaea

%global __requires_exclude .*BugzillaClient.*

Name:           vym
Version:        2.9.26
Release:        6%{?dist}
Summary:        View your mind

License:        GPL-2.0-or-later
URL:            https://github.com/insilmaril/vym/
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

Source1:        %{name}.desktop
Source2:        vym.xml
Source3:	vym-logo-new-16.png
Source4:	vym-logo-new-22.png
Source5:	vym-logo-new-24.png
Source6:	vym-logo-new-32.png
Source7:	vym-logo-new-48.png
Source8:	vym-logo-new-256.png

BuildRequires:  make cmake
BuildRequires:  qt5-qtbase-devel qt5-qtsvg-devel libXext-devel desktop-file-utils
BuildRequires:  qt5-qtscript-devel qt5-linguist

%{?filter_setup:
%filter_from_requires /^perl(BugzillaClient)$/d
%?perl_default_filter
}
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}perl\\(BugzillaClient\\)
Requires:	perl-BZ-Client
# For file operations, we use command-line utilities.
Requires: coreutils zip unzip

%description
VYM (View Your Mind) is a tool to generate and manipulate maps
which show your thoughts. Such maps can help you to improve
your creativity and effectivity. You can use them for time management,
to organize tasks, to get an overview over complex contexts.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

%global docval %{_docdir}

%cmake -DCMAKE_INSTALL_DATAROOTDIR:PATH=share/vym
%cmake_build

%install
mkdir -p %{buildroot}%{_datadir}/vym
%cmake_install

%{__mkdir} -p %{buildroot}%{_datadir}/applications/

desktop-file-install             \
    --dir %{buildroot}%{_datadir}/applications \
    %{SOURCE1}

%{__mkdir} -p %{buildroot}%{_datadir}/icons/hicolor/16x16/apps
%{__cp} -p %{SOURCE3} %{buildroot}%{_datadir}/icons/hicolor/16x16/apps/%{name}.png
%{__cp} -p icons/%{name}.xpm %{buildroot}%{_datadir}/icons/hicolor/16x16/apps/%{name}.xpm

%{__mkdir} -p %{buildroot}%{_datadir}/icons/hicolor/22x22/apps
%{__cp} -p %{SOURCE4} %{buildroot}%{_datadir}/icons/hicolor/22x22/apps/%{name}.png

%{__mkdir} -p %{buildroot}%{_datadir}/icons/hicolor/24x24/apps
%{__cp} -p %{SOURCE5} %{buildroot}%{_datadir}/icons/hicolor/24x24/apps/%{name}.png

%{__mkdir} -p %{buildroot}%{_datadir}/icons/hicolor/32x32/apps
%{__cp} -p %{SOURCE6} %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/%{name}.png

%{__mkdir} -p %{buildroot}%{_datadir}/icons/hicolor/48x48/apps
%{__cp} -p %{SOURCE7} %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
%{__cp} -p icons/%{name}-editor.png %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/%{name}-editor.png

%{__mkdir} -p %{buildroot}%{_datadir}/icons/hicolor/256x256/apps
%{__cp} -p %{SOURCE8} %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/%{name}.png

install -m a+rx,u+w -d %{buildroot}%{_datadir}/mime/packages
install -p -m a+r,u+w %{SOURCE2} %{buildroot}%{_datadir}/mime/packages/vym.xml

%files
%license LICENSE.txt
%doc README.md demos/* doc/*
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/16x16/apps/%{name}*
%{_datadir}/icons/hicolor/22x22/apps/%{name}*
%{_datadir}/icons/hicolor/24x24/apps/%{name}*
%{_datadir}/icons/hicolor/32x32/apps/%{name}*
%{_datadir}/icons/hicolor/48x48/apps/%{name}*
%{_datadir}/icons/hicolor/256x256/apps/%{name}*
%{_datadir}/mime/packages/vym.xml

%changelog
%autochangelog
