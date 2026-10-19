%global source0_hash 8a7a394ab30703fad32cf4073ff4f3f4e8c585d4cdd7877e1d8f2945724263b8
Name:		lightdm-settings
Version:	2.1.1
Release:        1%{?dist}
Summary:        Configuration tool for the LightDM display manager
License:	GPL-3.0-or-later
URL:		https://github.com/linuxmint/%{name}
Source0:        https://github.com/linuxmint/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:	noarch
Requires:	filesystem
Requires:	gtk3
Requires:	hicolor-icon-theme
Requires:	polkit
Requires:	python3-xapp
Requires:	python3-gobject
Requires:	python3-setproctitle
Requires:	slick-greeter
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  make
# /oreon:deps
%description
This tool currently lets users configure slick-greeter.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%make_build
%install
%{__cp} -pr .%{_prefix} %{buildroot}
%{__chmod} -c 0755 %{buildroot}%{_bindir}/%{name} \
	 %{buildroot}%{_prefix}/lib/%{name}/%{name}
%find_lang %{name}
%oreon_autofiles main

%check

%{_bindir}/desktop-file-validate \
	%{buildroot}%{_datadir}/applications/*.desktop
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
