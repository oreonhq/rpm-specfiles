%global source0_hash 83eab6ba893dce56f0523a70ebfcf2a78f7785637a6895255777ef1b72d4eb89
%global debug_package %{nil}
%global __brp_mangle_shebangs_exclude_from %{_bindir}/distrobox-(export|init|host-exec)$
%global forgeurl https://github.com/89luca89/distrobox
%global tag %{version}
Name:    distrobox
Version: 1.8.2.5
%forgemeta
Release:        1%{?dist}
Summary:        Another tool for containerized command line environments on Linux
License: GPL-3.0-only
URL:     %{forgeurl}
Source0:        %{forgeurl}/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch: noarch
Requires: (podman or %{_bindir}/docker)
Requires: %{_bindir}/basename
Requires: %{_bindir}/find
Requires: %{_bindir}/grep
Requires: %{_bindir}/sed
Requires: hicolor-icon-theme
Suggests: bash-completions
# oreon:deps

# /oreon:deps
%description
Use any linux distribution inside your terminal. Distrobox uses podman 
or docker to create containers using the linux distribution of your 
choice. Created container will be tightly integrated with the host, 
allowing to share the HOME directory of the user, external storage, 
external usb devices and graphical apps (X11/Wayland) and audio.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%install
./install -P %{buildroot}/%{_prefix}
%oreon_autofiles main

%check

%{buildroot}%{_bindir}/%{name} list -V
for i in create enter export init list rm stop host-exec; do
    %{buildroot}%{_bindir}/%{name}-$i -V
done
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
