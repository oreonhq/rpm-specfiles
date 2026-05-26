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
