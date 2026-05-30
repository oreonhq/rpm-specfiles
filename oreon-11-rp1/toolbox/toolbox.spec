%global source0_hash 0243bd995743ea73464426839ee80e2a13a8c529e3053292783f603b882dd125

%global __brp_check_rpaths %{nil}

%if 0%{?rhel}
%if 0%{?rhel} <= 9
%{!?bash_completions_dir: %global bash_completions_dir %{_datadir}/bash-completion/completions}
%{!?fish_completions_dir: %global fish_completions_dir %{_datadir}/fish/vendor_completions.d}
%{!?zsh_completions_dir: %global zsh_completions_dir %{_datadir}/zsh/site-functions}
%endif
%endif


Name:          toolbox
Version:       0.3

%global goipath github.com/containers/%{name}

%if 0%{?fedora}
%gometa -f
%endif

%if 0%{?rhel}
%if 0%{?rhel} <= 9
%gometa
%else
%gometa -f
%endif
%endif

%global toolbx_go 1.22

%if 0%{?fedora}
%global toolbx_go 1.24.7
%endif

%if 0%{?rhel}
%if 0%{?rhel} == 9
%global toolbx_go 1.22.5
%elif 0%{?rhel} == 10
%global toolbx_go 1.22.5
%elif 0%{?rhel} > 10
%global toolbx_go 1.24.4
%endif
%endif

Release:       4%{?dist}
Summary:       Tool for interactive command line environments on Linux

License:       Apache-2.0
URL:           https://containertoolbx.org/
Source0:        https://github.com/containers/%{name}/releases/download/%{version}/%{name}-%{version}-vendored.tar.xz

# RHEL specific
Source1:       %{name}.conf

# Fedora specific
Patch100:      toolbox-Make-the-build-flags-match-Fedora.patch

# RHEL specific
Patch200:      toolbox-Make-the-build-flags-match-RHEL-9.patch
Patch201:      toolbox-Make-the-build-flags-match-RHEL-10.patch
Patch202:      toolbox-Add-migration-paths-for-coreos-toolbox-users.patch

BuildRequires: gcc
BuildRequires: go-md2man
BuildRequires: golang >= %{toolbx_go}
BuildRequires: meson >= 0.58.0
BuildRequires: pkgconfig(bash-completion)
BuildRequires: shadow-utils-subid-devel >= 4.16.0
BuildRequires: systemd
BuildRequires: systemd-rpm-macros
%if ! 0%{?rhel}
BuildRequires: pkgconfig(fish)
# for tests
# BuildRequires: codespell
# BuildRequires: ShellCheck
%endif

Recommends:    p11-kit-server
Recommends:    skopeo
%if ! 0%{?rhel}
Recommends:    fuse-overlayfs
%endif

Requires:      containers-common
Requires:      flatpak-session-helper
Requires:      podman >= 1.6.4
Requires:      shadow-utils-subid%{?_isa} >= 4.16.0


%description
Toolbx is a tool for Linux, which allows the use of interactive command line
environments for software development and troubleshooting the host operating
system, without having to install software on the host. It is built on top of
Podman and other standard container technologies from OCI.

Toolbx environments have seamless access to the user's home directory, the
Wayland and X11 sockets, networking (including Avahi), removable devices (like
USB sticks), systemd journal, SSH agent, D-Bus, ulimits, /dev and the udev
database, etc..


%package       tests
Summary:       Tests for %{name}

Requires:      %{name}%{?_isa} = %{version}-%{release}
Requires:      coreutils
Requires:      diffutils
# for gdbus(1)
Requires:      glib2
Requires:      grep
# for htpasswd(1)
Requires:      httpd-tools
Requires:      openssl
Requires:      python3
Requires:      skopeo
%if ! 0%{?rhel}
Requires:      bats >= 1.10.0
%endif


%description   tests
The %{name}-tests package contains system tests for %{name}.


%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -q

%if 0%{?fedora}
%patch -P100 -p1
%endif

%if 0%{?rhel}
%if 0%{?rhel} == 9
%patch -P200 -p1
%endif

%if 0%{?rhel} >= 10
%patch -P201 -p1
%endif

%if 0%{?rhel} <= 9
%patch -P202 -p1
%endif
%endif

%gomkdir -s %{_builddir}/%{extractdir}/src -k


%build
export CGO_CFLAGS="%{optflags} -D_GNU_SOURCE -D_LARGEFILE_SOURCE -D_LARGEFILE64_SOURCE -D_FILE_OFFSET_BITS=64"

%meson \
%if 0%{?rhel}
    -Dfish_completions_dir=%{fish_completions_dir} \
%if 0%{?rhel} <= 9
    -Dmigration_path_for_coreos_toolbox=true \
%endif
%endif
    -Dprofile_dir=%{_sysconfdir}/profile.d \
    -Dtmpfiles_dir=%{_tmpfilesdir} \
    -Dzsh_completions_dir=%{zsh_completions_dir}

%meson_build


# %%check
# %%meson_test


%install
%meson_install

%if 0%{?rhel}
%if 0%{?rhel} <= 9
install -m0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/containers/%{name}.conf
%endif
%endif


%files
%doc CODE-OF-CONDUCT.md CONTRIBUTING.md GOALS.md NEWS README.md SECURITY.md
%license COPYING src/vendor/modules.txt
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_mandir}/man1/%{name}-*.1*
%{_mandir}/man5/%{name}.conf.5*
%config(noreplace) %{_sysconfdir}/containers/%{name}.conf
%{_sysconfdir}/profile.d/%{name}.sh
%{_tmpfilesdir}/%{name}.conf
%{bash_completions_dir}/%{name}.bash
%{fish_completions_dir}/%{name}.fish
%{zsh_completions_dir}/_%{name}


%files tests
%{_datadir}/%{name}


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.3-4
- Prepare for Oreon 11 (RP1)
