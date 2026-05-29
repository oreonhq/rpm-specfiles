%global source0_hash 771385049516fdd561fbb9164eddf376075c4c7de3900a8b18654660172748f1

Name: catatonit
Version: 0.2.1
Summary: A signal-forwarding process manager for containers
License: GPL-3.0-or-later
Release: %autorelease
%if %{defined copr_username}
# Set copr rpm build epoch to a very high value
Epoch: 101
%else
%if %{defined rhel}
# Bump epoch to 5 for RHEL
# Ref: https://bugzilla.redhat.com/show_bug.cgi?id=2257446
Epoch: 5
%endif
%endif
%if %{defined golang_arches_future}
ExclusiveArch: %{golang_arches_future}
%else
ExclusiveArch: aarch64 ppc64le s390x x86_64
%endif
URL: https://github.com/openSUSE/%{name}
# Tarball fetched from upstream
Source0:        https://github.com/openSUSE/catatonit/archive/refs/tags/v0.2.1.tar.gz

BuildRequires: autoconf
BuildRequires: automake
BuildRequires: file
BuildRequires: libtool
Provides: podman-%{name} = %{version}-%{release}
BuildRequires: gcc
BuildRequires: git-core
BuildRequires: glibc-static
BuildRequires: make

%description
Catatonit is a %{_sbindir}/init program for use within containers. It
forwards (almost) all signals to the spawned child, tears down
the container when the spawned child exits, and otherwise
cleans up other exited processes (zombies).

This is a reimplementation of other container init programs (such as
"tini" or "dumb-init"), but uses modern Linux facilities (such as
signalfd(2)) and has no additional features.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -S git %{name}-%{version}

%build
./autogen.sh
%configure
CFLAGS="%{optflags} -fPIE -D_GNU_SOURCE -D_LARGEFILE_SOURCE -D_LARGEFILE64_SOURCE"
%{__make} %{?_smp_mflags}

# Make sure we *always* build a static binary. Otherwise we'll break containers
# that don't have the necessary shared libs.
file ./%{name} | grep 'statically linked'
if [ $? != 0 ]; then
   echo "ERROR: %{name} binary must be statically linked!"
   exit 1
fi

%install
install -dp %{buildroot}%{_libexecdir}/%{name}
install -p %{name} %{buildroot}%{_libexecdir}/%{name}
install -dp %{buildroot}%{_libexecdir}/podman
ln -s %{_libexecdir}/%{name}/%{name} %{buildroot}%{_libexecdir}/podman/%{name}

%check

%files
%license COPYING
%doc README.md
%dir %{_libexecdir}/%{name}
%{_libexecdir}/%{name}/%{name}
%dir %{_libexecdir}/podman
%{_libexecdir}/podman/%{name}

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.2.1-1
- Prepare for Oreon 11 (RP1)
