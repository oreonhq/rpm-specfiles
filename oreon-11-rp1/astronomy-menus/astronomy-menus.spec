%global source0_hash 8948ec2c7f2142a19e539bba33f09a145ccd4e03842cdf900916f5bfa6ccd071
Name:           astronomy-menus
Version:        1.0
Release:        1%{?dist}
Summary:        Astronomy menu for the Desktop
License:        LicenseRef-Fedora-Public-Domain
URL:            http://fedoraproject.org/wiki/SIGs/Astronomy
Source0:        %{name}-%{version}.tar.gz
BuildArch:      noarch
Requires:       redhat-menus hicolor-icon-theme
# oreon:deps
BuildRequires:  m4
BuildRequires:  make
BuildRequires:  tidy
# /oreon:deps
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
%oreon_autofiles astronomy-menus-toplevel usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

make test
%files -f %{oreon_filedir}/main.list
%files -n astronomy-menus-toplevel -f %{oreon_filedir}/astronomy-menus-toplevel.list

%changelog

%autochangelog
