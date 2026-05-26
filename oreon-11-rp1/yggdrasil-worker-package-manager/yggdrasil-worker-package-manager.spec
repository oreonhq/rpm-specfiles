%bcond_without check

# https://github.com/redhatinsights/yggdrasil-worker-package-manager
%global goipath         github.com/redhatinsights/yggdrasil-worker-package-manager
Version:                0.2.3
%global tag             v%{version}

%gometa -f

%global common_description %{expand:
yggdrasil-worker-package-manager is a simple package manager yggd worker. It
knows how to install and remove packages, add, remove, enable and disable
repositories, and does rudimentary detection of the host it is running on to
guess the package manager to use. It only installs packages that match one of
the provided allow-pattern regular expressions.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           yggdrasil-worker-package-manager
Release:        %autorelease
Summary:        Package manager worker for yggdrasil

License:        GPL-3.0-only
URL:            %{gourl}
Source:         %{url}/releases/download/%{tag}/%{name}-%{version}.tar.xz
# oreon url source checksums begin
%global source0_sha256 3e24cd6b081b71140a775c4c79e9b46353d722d9b077b3deaf9d27bd75add215
%global source0_file yggdrasil-worker-package-manager-0.2.3.tar.xz
# oreon url source checksums end

BuildRequires:  systemd-rpm-macros
BuildRequires:  meson
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  golang >= 1.21

%description %{common_description}

%gopkg

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/yggdrasil-worker-package-manager-0.2.3.tar.xz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "3e24cd6b081b71140a775c4c79e9b46353d722d9b077b3deaf9d27bd75add215" || { echo "oreon: Source0 SHA256 mismatch for yggdrasil-worker-package-manager-0.2.3.tar.xz" >&2; exit 1; })
# oreon verify url source checksums end
%goprep %{?rhel:-k}

%if %{undefined rhel}
%generate_buildrequires
%go_generate_buildrequires
%endif

%build
%undefine _auto_set_build_flags
export %gomodulesmode
%{?gobuilddir:export GOPATH="%{gobuilddir}:${GOPATH:+${GOPATH}:}%{?gopath}"}
%meson "-Dgobuildflags=[%(echo %{expand:%gocompilerflags} | sed -e s/"^"/"'"/ -e s/" "/"', '"/g -e s/"$"/"'"/), '-tags', '"rpm_crashtraceback\ ${BUILDTAGS:-}"', '-a', '-v', '-x']" -Dgoldflags='%{?currentgoldflags} -B 0x%(head -c20 /dev/urandom|od -An -tx1|tr -d " \n") -compressdwarf=false -linkmode=external -extldflags "%{build_ldflags} %{?__golang_extldflags}"'
%meson_build

%install
%meson_install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%post
%systemd_post com.redhat.Yggdrasil1.Worker1.package_manager.service

%preun
%systemd_preun com.redhat.Yggdrasil1.Worker1.package_manager.service

%postun
%systemd_postun_with_restart com.redhat.Yggdrasil1.Worker1.package_manager.service

%files
%license LICENSE
%if %{defined rhel}
%license vendor/modules.txt
%endif
%doc README.md
%{_libexecdir}/*
%config(noreplace) %{_sysconfdir}/%{name}
%{_datadir}/dbus-1/system-services/*
%{_datadir}/dbus-1/system.d/*
%{_unitdir}

%gopkgfiles

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.2.3-1
- Prepare for Oreon 11 (RP1)
