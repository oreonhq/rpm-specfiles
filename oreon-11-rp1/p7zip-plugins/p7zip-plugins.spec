%global source0_hash none

Summary:        Compatibility package for p7zip plugins
Name:           p7zip-plugins
Version:        16.02
Release:        1%{?dist}
License:        LGPL-2.1-or-later
URL:            https://sourceforge.net/projects/p7zip/
BuildArch:      noarch

Source0:        LICENSE
Source1:        README.oreon

Provides:       p7zip-plugins = %{version}-%{release}

%description
Compatibility package to provide p7zip-plugins in Oreon repositories.
This package intentionally ships metadata and documentation only.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%build

%install
install -d -m 0755 %{buildroot}%{_docdir}/%{name}
install -m 0644 %{SOURCE0} %{buildroot}%{_docdir}/%{name}/
install -m 0644 %{SOURCE1} %{buildroot}%{_docdir}/%{name}/

%files
%license %{_docdir}/%{name}/LICENSE
%doc %{_docdir}/%{name}/README.oreon

%changelog
* Sun Apr 12 2026 Oreon Packaging Team <packaging@oreonhq.com> - 16.02-1
- Add p7zip-plugins compatibility package to Oreon repo
