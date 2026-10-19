%global source0_hash none
Name:           gnome-shell-rpm-generators
Version:        1
Release:        1%{?dist}
Summary:        RPM generators for gnome-shell
License:        MIT
URL:            https://src.fedoraproject.org/rpms/gnome-shell-rpm-generators
Source0:        LICENSE
BuildArch:      noarch
Requires:       jq
# oreon:deps

# /oreon:deps
%description
RPM generators for gnome-shell.

Currently it generates:

```
Provides: gnome-shell-extension(UUID)
Requires: (gnome-shell(api) = VER1 or gnome-shell(api) = VER2 or ...)
```

%prep

%autosetup -c -T
cp -a %{sources} .

%build

%install
install -Dpm0644 -t %{buildroot}%{_fileattrsdir} *.attr
install -Dpm0755 -t %{buildroot}%{_rpmconfigdir} *.sh
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
