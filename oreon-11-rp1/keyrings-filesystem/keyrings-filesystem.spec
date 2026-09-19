%global source0_hash none

Name:           keyrings-filesystem
Version:        1
Release:        25%{?dist}
Summary:        Keyrings filesystem layout

License:        LicenseRef-Fedora-Public-Domain
BuildArch:      noarch

Requires:       filesystem
Requires:       rpm

%description
This package provides the directory to store keyrings.

%prep
# Nothing to prep

%build
# Nothing to build

%install
# Directories
install -d %{buildroot}%{_rpmconfigdir}/macros.d
install -d %{buildroot}%{_datadir}/keyrings

# RPM macro
cat > %{buildroot}%{_rpmconfigdir}/macros.d/macros.keyrings <<EOF
%%_keyringsdir %%_datadir/keyrings
EOF

%files
%dir %{_datadir}/keyrings
%{_rpmconfigdir}/macros.d/macros.keyrings

%changelog
%autochangelog
