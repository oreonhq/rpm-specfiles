Name:           oreon-rpm-macros
Version:        1
Release:        1%{?dist}
Summary:        Build macros for Oreon packages
License:        MIT
URL:            https://github.com/oreonhq/rpm-specfiles

%global         source0_hash f8af9644538637372eb1c9ecc2bb779b407f1b7ca686d655f8edc6c73186c236

Source0:        macros.oreon
Source1:        oreon-build
Source2:        oreon-gpgverify
Source3:        oreon-pyfiles
Source4:        oreon-python.attr
Source5:        oreon-pythondeps

BuildArch:      noarch

%description
Macros and helpers that Oreon specs use to configure, build, and install
software.

%package python
Summary:        Python helpers for Oreon packages
Requires:       %{name} = %{version}-%{release}
Requires:       python3

%description python
File lists and dependency generation for Python packages.

%prep
echo "%{source0_hash}  %{SOURCE0}" | sha256sum -c -

%build
:

%install
install -D -p -m 644 %{SOURCE0} %{buildroot}%{_rpmconfigdir}/macros.d/macros.oreon
install -D -p -m 755 %{SOURCE1} %{buildroot}%{_libexecdir}/oreon-rpm-macros/oreon-build
install -D -p -m 755 %{SOURCE2} %{buildroot}%{_libexecdir}/oreon-rpm-macros/oreon-gpgverify
install -D -p -m 755 %{SOURCE3} %{buildroot}%{_libexecdir}/oreon-rpm-macros/oreon-pyfiles
install -D -p -m 644 %{SOURCE4} %{buildroot}%{_rpmconfigdir}/fileattrs/oreon-python.attr
install -D -p -m 755 %{SOURCE5} %{buildroot}%{_rpmconfigdir}/oreon/oreon-pythondeps

%files
%dir %{_libexecdir}/oreon-rpm-macros
%{_libexecdir}/oreon-rpm-macros/oreon-build
%{_libexecdir}/oreon-rpm-macros/oreon-gpgverify
%{_rpmconfigdir}/macros.d/macros.oreon

%files python
%{_libexecdir}/oreon-rpm-macros/oreon-pyfiles
%{_rpmconfigdir}/fileattrs/oreon-python.attr
%dir %{_rpmconfigdir}/oreon
%{_rpmconfigdir}/oreon/oreon-pythondeps

%changelog
* Mon Oct 19 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1-1
- init