%global source0_hash af95091bd2125d1afc9b03f65628c1dd5c7e609e6a4eebdd8f66b7e936de88f5

%global commit 233ebaca4b6d63b642e00f93030cb1bff8432855
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           canl-c
Version:        3.0.0
Release:        25.20250222git%{shortcommit}%{?dist}
Summary:        Common Authentication library - bindings for C

License:        Apache-2.0
URL:            https://github.com/CESNET/canl-c
Source:         https://github.com/CESNET/%{name}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

BuildRequires:  bison
BuildRequires:  c-ares-devel
BuildRequires:  flex
BuildRequires:  krb5-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  openssl-devel >= 1.1
BuildRequires:  perl-interpreter
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(POSIX)
BuildRequires:  pkgconfig
BuildRequires:  tex(latex)
BuildRequires:  tex(lastpage.sty)
BuildRequires:  tex(multirow.sty)

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
# in -doc subpackage
rm -f %{buildroot}%{_defaultdocdir}/%{name}-%{version}/README
rm -f %{buildroot}%{_defaultdocdir}/%{name}-%{version}/canl.pdf
rm -f %{buildroot}%{_libdir}/*.a
rm -f %{buildroot}%{_libdir}/*.la

%ldconfig_scriptlets

%files
%license LICENSE
%doc ChangeLog README
%{_libdir}/libcanl_c.so.4
%{_libdir}/libcanl_c.so.4.*

%files devel
%{_includedir}/*.h
%{_libdir}/libcanl_c.so

%files doc
%license LICENSE
%doc canl.pdf

%files examples
%{_bindir}/*

%changelog
%autochangelog
