%global source0_hash 8a7a394ab30703fad32cf4073ff4f3f4e8c585d4cdd7877e1d8f2945724263b8

Name:		lightdm-settings
Version:	2.1.1
Release:	2%{?dist}
Summary:	Configuration tool for the LightDM display manager

License:	GPL-3.0-or-later
URL:		https://github.com/linuxmint/%{name}
Source0:	%{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:	noarch

BuildRequires:	desktop-file-utils
BuildRequires:	gettext
BuildRequires:	make

Requires:	filesystem
Requires:	gtk3
Requires:	hicolor-icon-theme
Requires:	polkit
Requires:	python3-xapp
Requires:	python3-gobject
Requires:	python3-setproctitle
Requires:	slick-greeter

%description
This tool currently lets users configure slick-greeter.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p 1

%build
%make_build

%install
# No install-target in Makefile.
%{__cp} -pr .%{_prefix} %{buildroot}

# Set exec-permissions where needed.
%{__chmod} -c 0755 %{buildroot}%{_bindir}/%{name} \
	 %{buildroot}%{_prefix}/lib/%{name}/%{name}

# Find localizations and build manifest.
%find_lang %{name}

%check
%{_bindir}/desktop-file-validate \
	%{buildroot}%{_datadir}/applications/*.desktop

%files -f %{name}.lang
%license debian/copyright COPYING
%doc debian/changelog README.md
%{_bindir}/%{name}
%{_prefix}/lib/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_datadir}/polkit-1/actions/org.x.%{name}.policy

%changelog
%autochangelog
