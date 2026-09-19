%global source0_hash 8948ec2c7f2142a19e539bba33f09a145ccd4e03842cdf900916f5bfa6ccd071

Name:           astronomy-menus
Version:        1.0
Release:        34%{?dist}
Summary:        Astronomy menu for the Desktop
License:        LicenseRef-Fedora-Public-Domain
URL:            http://fedoraproject.org/wiki/SIGs/Astronomy
# git clone git://git.fedorahosted.org/git/astronomy.git
# make -C astronomy/projects/astronomy-menus dist
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch
Requires:       redhat-menus hicolor-icon-theme
BuildRequires:  m4 tidy
BuildRequires: make

%description
Astronomy submenu for the Education menu, for better usability of the
Fedora Astronomy packages.

%package toplevel
Summary:        Toplevel astronomy menu for the Desktop

%description toplevel
Astronomy submenu for the Education menu, for better usability of the
Fedora Astronomy packages.

This package places the submenu at the Application menu root, which
may make sense if there are no other Education packages, such as in
Fedora Astronomy Live Media Spin.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
make %{_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%check
make test

%files
%config(noreplace) %{_sysconfdir}/xdg/menus/applications-merged/astronomy.menu
%{_datadir}/desktop-directories/Astronomy.directory
%{_datadir}/icons/hicolor/scalable/devices/dome.svg
%doc README

%files toplevel
%config(noreplace) %{_sysconfdir}/xdg/menus/applications-merged/astronomy-toplevel.menu
%{_datadir}/desktop-directories/Astronomy.directory
%{_datadir}/icons/hicolor/scalable/devices/dome.svg
%doc README

%changelog
%autochangelog
