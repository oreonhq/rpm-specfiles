%global source1_hash bf1cd41897dff67dbb20b5448677fee250faa2cefcbe5542d91f0f1d7ee266d5
%global source0_hash 73d419c6e20e874adaa4019372cbd097eecf4d276e13f27ec5e67d35c0bd203c
%global source2_key_fpr 63191CE94183098689CAB8DB7EF137EC935B0EAF
%define ruby_inc %(pkg-config --cflags ruby)
%define libsepolver 3.11-1
Summary:        SELinux library and simple utilities
Name: libselinux
Version: 3.11
Release:        1%{?dist}
License: LicenseRef-Fedora-Public-Domain
Source0:        https://github.com/SELinuxProject/selinux/releases/download/%{version}/libselinux-%{version}.tar.gz
Source1:        https://github.com/SELinuxProject/selinux/releases/download/%{version}/libselinux-%{version}.tar.gz.asc
Source2:        bachradsusi.gpg
Source3: selinuxconlist.8
Source4: selinuxdefcon.8
Url: https://github.com/SELinuxProject/selinux/wiki
Patch0001: 0001-Use-SHA-2-instead-of-SHA-1.patch
Patch0002: 0002-libselinux-Replace-PyString_FromString-with-PyUnicod.patch
Patch0003: 0003-libselinux-restorecon_xattr-reset-dir_xattr_list-on-.patch
Patch0004: 0004-Add-support-for-UTF-8-in-file-context-specifications.patch
Requires: libsepol%{?_isa} >= %{libsepolver} pcre2
Conflicts: filesystem < 3, selinux-policy-base < 3.13.1-138
# oreon:deps
BuildRequires:  (python3-wheel if python3-setuptools < 71)
BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  libsepol-static
BuildRequires:  make
BuildRequires:  pcre2-devel
BuildRequires:  python3
BuildRequires:  python3-build
BuildRequires:  python3-devel
BuildRequires:  python3-pip
BuildRequires:  python3-setuptools
BuildRequires:  ruby
BuildRequires:  ruby-devel
BuildRequires:  swig
BuildRequires:  systemd
# /oreon:deps
%description
Security-enhanced Linux is a feature of the Linux® kernel and a number
of utilities with enhanced security functionality designed to add
mandatory access controls to Linux.  The Security-enhanced Linux
kernel contains new architectural components originally developed to
improve the security of the Flask operating system. These
architectural components provide general support for the enforcement
of many kinds of mandatory access control policies, including those
based on the concepts of Type Enforcement®, Role-based Access
Control, and Multi-level Security.

libselinux provides an API for SELinux applications to get and set
process and file security contexts and to obtain security policy
decisions.  Required for any applications that use the SELinux API.

%package utils
Summary: SELinux libselinux utilities
Requires: %{name}%{?_isa} = %{version}-%{release}
%description utils
The libselinux-utils package contains the utilities

%package -n python3-libselinux
Summary: SELinux python 3 bindings for libselinux
Requires: %{name}%{?_isa} = %{version}-%{release}
%{?python_provide:%python_provide python3-libselinux}
Provides: %{name}-python3 = %{version}-%{release}
Provides: %{name}-python3%{?_isa} = %{version}-%{release}
Obsoletes: %{name}-python3 < %{version}-%{release}
%description -n python3-libselinux
The libselinux-python3 package contains python 3 bindings for developing
SELinux applications. 

%package ruby
Summary: SELinux ruby bindings for libselinux
Requires: %{name}%{?_isa} = %{version}-%{release}
Provides: ruby(selinux)
%description ruby
The libselinux-ruby package contains the ruby bindings for developing 
SELinux applications. 

%package devel
Summary: Header files and libraries used to build SELinux
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: libsepol-devel%{?_isa} >= %{libsepolver}
%description devel
The libselinux-devel package contains the libraries and header files
needed for developing SELinux applications. 

%package static
Summary: Static libraries used to build SELinux
Requires: %{name}-devel%{?_isa} = %{version}-%{release}
%description static
The libselinux-static package contains the static libraries
needed for developing SELinux applications. 

%prep

%(test -z "%{source2_key_fpr}" || { f="%{SOURCE2}"; test -f "$f" || { echo "oreon: missing Source2 key $f" >&2; exit 1; }; fpr=$(GNUPGHOME=$(mktemp -d); export GNUPGHOME; trap 'rm -rf "$GNUPGHOME"' EXIT; gpg --batch --with-colons --import-options show-only --import "$f" | awk -F: '/^fpr:/ {print toupper($10); exit}'); test "$fpr" = "%{source2_key_fpr}" || { echo "oreon: Source2 key fingerprint mismatch" >&2; exit 1; }; })
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p 2 -n libselinux-%{version}

%build

export DISABLE_RPM="y"
export USE_PCRE2="y"
%set_build_flags
CFLAGS="$CFLAGS -fno-semantic-interposition"
BuildPythonWrapper() {
  BinaryName=$1
  %make_build \
    PYTHON=$BinaryName \
    LIBDIR="%{_libdir}" \
    pywrap
}
%make_build LIBDIR="%{_libdir}" swigify
%make_build LIBDIR="%{_libdir}" all
BuildPythonWrapper %{__python3}
%make_build RUBYINC="%{ruby_inc}" SHLIBDIR="%{_libdir}" LIBDIR="%{_libdir}" LIBSEPOLA="%{_libdir}/libsepol.a" rubywrap
%install
InstallPythonWrapper() {
  BinaryName=$1
  make \
    PYTHON=$BinaryName \
    PIP_NO_BUILD_ISOLATION=0 \
    DESTDIR="%{buildroot}" LIBDIR="%{_libdir}" \
    SHLIBDIR="%{_lib}" BINDIR="%{_bindir}" \
    SBINDIR="%{_sbindir}" \
    LIBSEPOLA="%{_libdir}/libsepol.a" \
    install-pywrap
}
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_tmpfilesdir}
mkdir -p %{buildroot}%{_libdir}
mkdir -p %{buildroot}%{_includedir}
mkdir -p %{buildroot}%{_sbindir}
install -d -m 0755 %{buildroot}%{_rundir}/setrans
echo "d %{_rundir}/setrans 0755 root root" > %{buildroot}%{_tmpfilesdir}/libselinux.conf
InstallPythonWrapper %{__python3}
%make_install LIBDIR="%{_libdir}" SHLIBDIR="%{_libdir}" BINDIR="%{_bindir}" SBINDIR="%{_sbindir}"
make DESTDIR="%{buildroot}" RUBYINSTALL=%{ruby_vendorarchdir} install-rubywrap
rm -f %{buildroot}%{_sbindir}/compute_*
rm -f %{buildroot}%{_sbindir}/deftype
rm -f %{buildroot}%{_sbindir}/execcon
rm -f %{buildroot}%{_sbindir}/getenforcemode
rm -f %{buildroot}%{_sbindir}/getfilecon
rm -f %{buildroot}%{_sbindir}/getpidcon
rm -f %{buildroot}%{_sbindir}/mkdircon
rm -f %{buildroot}%{_sbindir}/policyvers
rm -f %{buildroot}%{_sbindir}/setfilecon
rm -f %{buildroot}%{_sbindir}/selinuxconfig
rm -f %{buildroot}%{_sbindir}/selinuxdisable
rm -f %{buildroot}%{_sbindir}/getseuser
rm -f %{buildroot}%{_sbindir}/togglesebool
rm -f %{buildroot}%{_sbindir}/selinux_check_securetty_context
mv %{buildroot}%{_sbindir}/getdefaultcon %{buildroot}%{_sbindir}/selinuxdefcon
mv %{buildroot}%{_sbindir}/getconlist %{buildroot}%{_sbindir}/selinuxconlist
install -d %{buildroot}%{_mandir}/man8/
install -m 644 %{SOURCE3} %{buildroot}%{_mandir}/man8/
install -m 644 %{SOURCE4} %{buildroot}%{_mandir}/man8/
rm -f %{buildroot}%{_mandir}/man8/togglesebool*
%ldconfig_scriptlets
%oreon_autofiles python3-libselinux usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/*/lib*.so.* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.*

%files -f %{oreon_filedir}/main.list
%files -n libselinux-utils -f %{oreon_filedir}/libselinux-utils.list
%files -n python3-libselinux -f %{oreon_filedir}/python3-libselinux.list
%files -n libselinux-ruby -f %{oreon_filedir}/libselinux-ruby.list
%files -n libselinux-devel -f %{oreon_filedir}/libselinux-devel.list
%files -n libselinux-static -f %{oreon_filedir}/libselinux-static.list

%changelog

%autochangelog
