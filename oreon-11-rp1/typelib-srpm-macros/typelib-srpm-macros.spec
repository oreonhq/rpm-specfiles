%global source0_hash none

Name:           typelib-srpm-macros
Version:        1
Release:        16%{?dist}
Summary:        gobject-introspection typelib sub-package generator macros

URL:            https://src.fedoraproject.org/rpms/typelib-srpm-macros
License:        LicenseRef-Fedora-Public-Domain
Source0:        macros.typelib

BuildArch:      noarch

%description
RPM macros for generating typelib sub-packages for gobject-introspection
enabled library packages

%prep
echo "These files herefore released into the Public Domain" > COPYING

%install
install -D -p %{SOURCE0} $RPM_BUILD_ROOT%{_rpmmacrodir}/macros.typelib

%files
%license COPYING
%{_rpmmacrodir}/macros.typelib

%changelog
%autochangelog
