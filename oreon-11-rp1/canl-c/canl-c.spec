%global source0_hash af95091bd2125d1afc9b03f65628c1dd5c7e609e6a4eebdd8f66b7e936de88f5
%global commit 233ebaca4b6d63b642e00f93030cb1bff8432855
%global shortcommit %(c=%{commit}; echo ${c:0:7})
Name:           canl-c
Version:        3.0.0
Release:        1%{?dist}
Summary:        Common Authentication library - bindings for C
License:        Apache-2.0
URL:            https://github.com/CESNET/canl-c
Source0:        https://github.com/CESNET/%{name}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
# oreon:deps
BuildRequires:  bison
BuildRequires:  c-ares-devel
BuildRequires:  flex
BuildRequires:  krb5-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(POSIX)
BuildRequires:  perl-interpreter
BuildRequires:  pkgconfig
BuildRequires:  tex(lastpage.sty)
BuildRequires:  tex(latex)
BuildRequires:  tex(multirow.sty)
# /oreon:deps
%description
This is the C part of the caNl -- the Common Authentication Library.

%package        devel
Summary:        Development files for caNl
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       krb5-devel%{?_isa}
%description    devel
This package contains development libraries and header files for caNl.

%package        doc
Summary:        API documentation for caNl
BuildArch:      noarch
%description    doc
This package contains API documentation for caNl.

%package        examples
Summary:        Example programs of caNl
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    examples
This package contains client and server examples of caNl.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{commit}

%build

./configure --root=/ --prefix=%{_prefix} --libdir=%{_lib}
CFLAGS="%{?optflags}" LDFLAGS="%{?__global_ldflags}" make %{?_smp_mflags}
%install
make install DESTDIR=%{buildroot}
rm -f %{buildroot}%{_defaultdocdir}/%{name}-%{version}/README
rm -f %{buildroot}%{_defaultdocdir}/%{name}-%{version}/canl.pdf
rm -f %{buildroot}%{_libdir}/*.a
rm -f %{buildroot}%{_libdir}/*.la
%ldconfig_scriptlets
%oreon_autofiles canl-c-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles canl-c-doc usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles canl-c-examples usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n canl-c-devel -f %{oreon_filedir}/canl-c-devel.list
%files -n canl-c-doc -f %{oreon_filedir}/canl-c-doc.list
%files -n canl-c-examples -f %{oreon_filedir}/canl-c-examples.list

%changelog

%autochangelog
