%global source0_hash 79a2da5164d28d24e52716c479ad5da6d052133f956085a8966607ffdf466305

# Disable in source builds on EPEL <9
%undefine __cmake_in_source_build
%undefine __cmake3_in_source_build

%define csexec_archs aarch64 ppc64le s390x x86_64

Name:       cswrap
Version:    2.2.5
Release:    4%{?dist}
Summary:    Generic compiler wrapper

License:    GPL-3.0-or-later
URL:        https://github.com/csutils/%{name}
Source0:    https://github.com/csutils/%{name}/releases/download/%{name}-%{version}/%{name}-%{version}.tar.xz
Source1:    https://github.com/csutils/%{name}/releases/download/%{name}-%{version}/%{name}-%{version}.tar.xz.asc

# gpg --keyserver pgp.mit.edu --recv-key 992A96E075056E79CD8214F9873DB37572A37B36
# gpg --output kdudka.pgp --armor --export kdudka@redhat.com
Source2:    kdudka.pgp

BuildRequires: asciidoc
BuildRequires: cmake3
BuildRequires: gcc
BuildRequires: gnupg2

# csmock copies the resulting cswrap binary into mock chroot, which may contain
# an older (e.g. RHEL-7) version of glibc, and it would not dynamically link
# against the old version of glibc if it was built against a newer one.
# Therefore, we link glibc statically.
BuildRequires: glibc-static

# The test-suite runs automatically trough valgrind if valgrind is available
# on the system.  By not installing valgrind into mock's chroot, we disable
# this feature for production builds on architectures where valgrind is known
# to be less reliable, in order to avoid unnecessary build failures (see RHBZ
# #810992, #816175, and #886891).  Nevertheless developers are free to install
# valgrind manually to improve test coverage on any architecture.
%ifarch %{ix86} x86_64
BuildRequires: valgrind
%endif

%description
Generic compiler wrapper used by csmock to capture diagnostic messages.

# csexec is available on architectures defined in %%{csexec_archs} only
%ifarch %{csexec_archs}
%package -n csexec
Summary: Dynamic linker wrapper
Conflicts: csexec < %{version}-%{release}

%description -n csexec
This package contains csexec - a dynamic linker wrapper.  The wrapper can
be used to run dynamic analyzers and formal verifiers on source RPM package
fully automatically.
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup

%build
%cmake3 \
    -DPATH_TO_WRAP=\"%{_libdir}/cswrap\" \
    -DSTATIC_LINKING=ON
%cmake3_build

%check
%ctest3

%install
%cmake3_install

install -m0755 -d "%{buildroot}%{_libdir}"{,/cswrap}
for i in c++ cc g++ gcc clang clang++ cppcheck smatch \
    divc++ divcc diosc++ dioscc gclang++ gclang goto-gcc \
    %{_arch}-redhat-linux-c++ \
    %{_arch}-redhat-linux-g++ \
    %{_arch}-redhat-linux-gcc
do
    ln -s ../../bin/cswrap "%{buildroot}%{_libdir}/cswrap/$i"
done

%files
%license COPYING
%doc README
%{_bindir}/cswrap
%{_libdir}/cswrap
%{_mandir}/man1/%{name}.1*

%ifarch %{csexec_archs}
%files -n csexec
%license COPYING
%{_bindir}/csexec
%{_bindir}/csexec-loader
%{_libdir}/libcsexec-preload.so
%{_mandir}/man1/csexec.1*
%endif

%changelog
%autochangelog
