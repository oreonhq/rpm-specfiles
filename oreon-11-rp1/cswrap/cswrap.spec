%global source1_hash 777dd35963db09fa75816d24dd535d4b982bf451680dff21c91fff604146673c
%global source0_hash 79a2da5164d28d24e52716c479ad5da6d052133f956085a8966607ffdf466305
%undefine __cmake_in_source_build
%undefine __cmake3_in_source_build
%define csexec_archs aarch64 ppc64le s390x x86_64
Name:       cswrap
Version:    2.2.5
Release:        1%{?dist}
Summary:        Generic compiler wrapper
License:    GPL-3.0-or-later
URL:        https://github.com/csutils/%{name}
Source0:        https://github.com/csutils/%{name}/releases/download/%{name}-%{version}/%{name}-%{version}.tar.xz
Source1:    https://github.com/csutils/%{name}/releases/download/%{name}-%{version}/%{name}-%{version}.tar.xz.asc
Source2:    kdudka.pgp
%ifarch %{ix86} x86_64
%endif
# oreon:deps
BuildRequires:  asciidoc
BuildRequires:  cmake3
BuildRequires:  gcc
BuildRequires:  glibc-static
BuildRequires:  gnupg2
# /oreon:deps
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
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
