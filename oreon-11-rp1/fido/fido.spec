%global source0_hash 9149c1201661c8172e5402eb22042ce4f416e2229b0d6bbfcc6baaed701d9676
Name:           fido
Version:        1.1.5
Release:        1%{?dist}
Summary:        Multi-threaded file watch utility
License:        GPL-2.0-or-later AND LicenseRef-Callaway-LGPLv2+
URL:            http://www.joedog.org/%{name}-home/
Source0:        http://download.joedog.org/%{name}/%{name}-%{version}.tar.gz
Patch0:         %{name}-shared-library.patch
%{?systemd_requires}
# oreon:deps
BuildRequires:  libjoedog-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description
A multi-threaded file watch utility. It can monitor files for changes in
content or modification times. If it notices a change, it will kick off a
user-defined script.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p 0
rm -f *.m4
rm -rf include/joedog/*.h
sed -i -e 's/AC_PROG_SHELL//' configure.ac
autoreconf --install --force

%build

export CFLAGS="-std=gnu17 %{build_cflags}"
%configure
%make_build
%install
%make_install
install -D -p -m 0644 utils/%{name}.service %{buildroot}%{_unitdir}/%{name}.service
for _file in doc/*.conf
do
    ln -f "${_file}" "${_file}.sample"
done
sed -e 's/^verbose  = true/verbose = false/' \
  %{buildroot}%{_sysconfdir}/%{name}/%{name}.conf.sample \
  > %{buildroot}%{_sysconfdir}/%{name}/%{name}.conf
rm -f %{buildroot}%{_sysconfdir}/%{name}/%{name}.conf.sample
%oreon_autofiles main

%post

%systemd_post %{name}.service
%preun

%systemd_preun %{name}.service
%postun

%systemd_postun_with_restart %{name}.service
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
