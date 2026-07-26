%global source0_hash 2d0e88d9ffae3a85dafc957a99f64e5f174e4563fd048b9b645ebc3be9e1ace4

# Disable in source builds on EPEL <9
%undefine __cmake_in_source_build
%undefine __cmake3_in_source_build

Name:       cscppc
Version:    2.2.7
Release:    4%{?dist}
Summary:    A compiler wrapper that runs Cppcheck in background

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

# csmock copies the resulting cscppc binary into mock chroot, which may contain
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

%if 0%{?rhel} != 7
# cscppc is linked statically and can be used by csmock in chroot environment
# the {cwe} field in --template option is supported since cppcheck-1.85
Recommends: cppcheck >= 1.85
%endif

# older versions of csdiff do not read CWE numbers from Cppcheck output
Conflicts: csdiff < 1.8.0

%description
This package contains the cscppc compiler wrapper that runs Cppcheck in
background fully transparently.

%package -n csclng
Summary: A compiler wrapper that runs Clang in background
Requires: clang
Conflicts: csmock-plugin-clang < 1.5.0

%description -n csclng
This package contains the csclng compiler wrapper that runs the Clang analyzer
in background fully transparently.

%package -n csgcca
Summary: A compiler wrapper that runs GCC analyzer in background
Requires: gcc

%description -n csgcca
This package contains the csgcca compiler wrapper that runs GCC analyzer
in background fully transparently.

%package -n csmatch
Summary: A compiler wrapper that runs Smatch in background
%if 0%{?rhel} != 7
Recommends: smatch
%endif

%description -n csmatch
This package contains the csmatch compiler wrapper that runs the Smatch analyzer
in background fully transparently.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup

%build
%cmake3                                       \
    -DPATH_TO_CSCPPC=\"%{_libdir}/cscppc\"    \
    -DPATH_TO_CSCLNG=\"%{_libdir}/csclng\"    \
    -DPATH_TO_CSGCCA=\"%{_libdir}/csgcca\"    \
    -DPATH_TO_CSMATCH=\"%{_libdir}/csmatch\"  \
    -DSTATIC_LINKING=ON
%cmake3_build

%check
%ctest3

%install
%cmake3_install

install -m0755 -d "%{buildroot}%{_libdir}"{,/cs{cppc,clng,gcca,match}}

for i in {,g}cc clang %{_arch}-redhat-linux-gcc
do
    ln -s ../../bin/cscppc  "%{buildroot}%{_libdir}/cscppc/$i"
    ln -s ../../bin/csclng  "%{buildroot}%{_libdir}/csclng/$i"
    ln -s ../../bin/csgcca  "%{buildroot}%{_libdir}/csgcca/$i"
    ln -s ../../bin/csmatch "%{buildroot}%{_libdir}/csmatch/$i"
done

for i in {c,g,clang}++ %{_arch}-redhat-linux-{c,g}++
do
    ln -s ../../bin/cscppc   "%{buildroot}%{_libdir}/cscppc/$i"
    ln -s ../../bin/csclng++ "%{buildroot}%{_libdir}/csclng/$i"
done

%files
%license COPYING
%doc README
%{_bindir}/cscppc
%{_datadir}/cscppc
%{_libdir}/cscppc
%{_mandir}/man1/%{name}.1*

%files -n csclng
%license COPYING
%{_bindir}/csclng
%{_bindir}/csclng++
%{_libdir}/csclng
%{_mandir}/man1/csclng.1*

%files -n csgcca
%license COPYING
%{_bindir}/csgcca
%{_libdir}/csgcca
%{_mandir}/man1/csgcca.1*

%files -n csmatch
%license COPYING
%{_bindir}/csmatch
%{_libdir}/csmatch
%{_mandir}/man1/csmatch.1*

%changelog
%autochangelog
