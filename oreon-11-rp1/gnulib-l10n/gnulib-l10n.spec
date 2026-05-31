%global source0_hash 155752ba6796aa294cde87c2bf0e771a5891eeeacb131345be0e080a3ec0ceea

Summary:        Compatibility package for gnulib-l10n
Name:           gnulib-l10n
Version:        20241231
Release:        1%{?dist}
License:        GPL-3.0-or-later
URL:            https://www.gnu.org/software/gnulib/
BuildArch:      noarch

Source0:        https://ftp.gnu.org/gnu/gnulib/%{name}-%{version}.tar.gz
Source1:        https://ftp.gnu.org/gnu/gnulib/%{name}-%{version}.tar.gz.sig

Provides:       gnulib-l10n = %{version}-%{release}

%description
Compatibility package to provide gnulib-l10n in Oreon repositories.
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
* Sun Apr 12 2026 Oreon Packaging Team <packaging@oreonhq.com> - 20241231-1
- Add gnulib-l10n compatibility package to Oreon repo
