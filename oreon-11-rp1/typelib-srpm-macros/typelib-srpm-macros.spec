%global source0_hash none
Name:           typelib-srpm-macros
Version:        1
Release:        16%{?dist}
Summary:        gobject-introspection typelib sub-package generator macros
URL:            https://src.fedoraproject.org/rpms/typelib-srpm-macros
License:        LicenseRef-Fedora-Public-Domain
Source0:        macros.typelib
BuildArch:      noarch
# oreon:deps

# /oreon:deps
%description
RPM macros for generating typelib sub-packages for gobject-introspection
enabled library packages

%prep

echo "These files herefore released into the Public Domain" > COPYING

%install
install -D -p %{SOURCE0} $RPM_BUILD_ROOT%{_rpmmacrodir}/macros.typelib
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
