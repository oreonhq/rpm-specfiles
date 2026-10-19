%global source0_hash fb79989da922c72fafdc9a5fc68fd0c8e78b7a42328fd17ac4579e864616222e
%global realname corba
%global debug_package %{nil}
%ifarch %{arm} %{mips} riscv64 %{ix86}
%bcond_with doc
%else
%bcond_without doc
%endif
Name:		erlang-%{realname}
Version:	5.2.2
Epoch:		1
Release:        1%{?dist}
Summary:        Erlang CORBA libraries
License:	Apache-2.0
URL:		https://github.com/erlang/%{realname}
VCS:		git:%{url}.git
Source0:        https://github.com/erlang/%{realname}/archive/%{version}/%{realname}-%{version}.tar.gz
Patch:		erlang-corba-0001-Add-files-from-OTP-tree.patch
Patch:		erlang-corba-0002-Edit-OTP-files-to-allow-out-of-tree-build.patch
Patch:		erlang-corba-0003-Do-not-install-C-sources.patch
Patch:		erlang-corba-0004-Do-not-install-Java-sources.patch
Patch:		erlang-corba-0005-Do-not-install-erlang-sources.patch
Patch:		erlang-corba-0006-Do-not-install-examples.patch
Patch:		erlang-corba-0007-Fix-javadoc.patch
%if %{with doc}
%endif
ExclusiveArch:	%{java_arches}
# oreon:deps
BuildRequires:  erlang-erl_docgen
BuildRequires:  erlang-erl_interface
BuildRequires:  erlang-erts
BuildRequires:  erlang-ftp
BuildRequires:  erlang-jinterface
BuildRequires:  erlang-parsetools
BuildRequires:  erlang-rpm-macros
BuildRequires:  fop
BuildRequires:  gcc
BuildRequires:  java-25-devel
BuildRequires:  libxslt
BuildRequires:  make
# /oreon:deps
%description
A set of Erlang applications, that implements a CORBA compliant Object Request
Broker (ORB) and a number of Object Managemnt Group (OMG) standard services.

%if %{with doc}
%package doc
Summary: Erlang CORBA documentation
BuildArch: noarch
%description doc
Documentation for Erlang.
%endif

%package -n erlang-cosEvent
Summary: Orber OMG Event Service
Requires: erlang-orber%{?_isa}
%description -n erlang-cosEvent
Orber OMG Event Service.

%package -n erlang-cosEventDomain
Summary: Orber OMG Event Domain Service
Requires: erlang-cosNotification%{?_isa}
Requires: erlang-orber%{?_isa}
%description -n erlang-cosEventDomain
Orber OMG Event Domain Service.

%package -n erlang-cosFileTransfer
Summary: Orber OMG File Transfer Service
Requires: erlang-cosProperty%{?_isa}
Requires: erlang-orber%{?_isa}
%description -n erlang-cosFileTransfer
Orber OMG File Transfer Service.

%package -n erlang-cosNotification
Summary: Orber OMG Notification Service
Requires: erlang-cosEvent%{?_isa}
Requires: erlang-cosTime%{?_isa}
Requires: erlang-orber%{?_isa}
%description -n erlang-cosNotification
Orber OMG Notification Service.

%package -n erlang-cosProperty
Summary: Orber OMG Property Service
Requires: erlang-orber%{?_isa}
%description -n erlang-cosProperty
Orber OMG Property Service.

%package -n erlang-cosTime
Summary: Orber OMG Timer and TimerEvent Service
Requires: erlang-cosEvent%{?_isa}
Requires: erlang-orber%{?_isa}
%description -n erlang-cosTime
Orber OMG Timer and TimerEvent Service.

%package -n erlang-cosTransactions
Summary: Orber OMG Transaction Service
Requires: erlang-orber%{?_isa}
%description -n erlang-cosTransactions
Orber OMG Transaction Service.

%package -n erlang-ic
Summary: IDL compiler
Requires: erlang-jinterface
Requires: javapackages-tools
%description -n erlang-ic
IDL compiler.

%package -n erlang-orber
Summary: A CORBA Object Request Broker
%description -n erlang-orber
A CORBA Object Request Broker.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{realname}-%{version}

%build

CFLAGS="$RPM_OPT_FLAGS" ERL_TOP=`pwd` make %{?_smp_mflags} V=1
%if %{with doc}
CFLAGS="$RPM_OPT_FLAGS" ERL_TOP=`pwd` make docs V=1
%endif
%install
ERL_TOP=`pwd` make install DESTDIR=%{buildroot}%{_erldir}
%if %{with doc}
ERL_TOP=`pwd` make install-docs DESTDIR=%{buildroot}%{_erldir}
%endif
install -m 0755 -d "%{buildroot}%{_javadir}/erlang"
ic_lib_dir="$(ls -d1 %{buildroot}%{_libdir}/erlang/lib/ic-*/ | sed "s,^%{buildroot},,")"
test -d "%{buildroot}$ic_lib_dir"
ln -s "${ic_lib_dir}priv/ic.jar" "%{buildroot}%{_javadir}/erlang/"
%if %{with doc}
for manpage in %{buildroot}%{_libdir}/erlang/man/man3/*
do
	mv ${manpage} ${manpage}erl
done
mkdir -p %{buildroot}%{_mandir}/
mv %{buildroot}%{_libdir}/erlang/man/* %{buildroot}%{_mandir}/
%endif
%if %{with doc}
mkdir -p %{buildroot}%{_docdir}/%{name}-%{version}/lib
pushd .
cd %{buildroot}%{_libdir}/erlang
mv -v doc %{buildroot}%{_docdir}/%{name}-%{version}
cd %{buildroot}%{_libdir}/erlang/lib
for i in * ; do mv -v $i/doc %{buildroot}%{_docdir}/%{name}-%{version}/lib/$i || true ; done
popd
for i in ic orber ; do mv -v lib/$i/examples %{buildroot}%{_docdir}/%{name}-%{version}/lib/$i-%{version}/examples || true ; done
cp -av AUTHORS CONTRIBUTING.md README.md %{buildroot}%{_docdir}/%{name}-%{version}
rm -f %{buildroot}%{_libdir}/erlang/README.md %{buildroot}%{_libdir}/erlang/COPYRIGHT
%endif
find %{buildroot}%{_libdir}/erlang -type f -name info -exec rm -f {} \;
%oreon_autofiles erlang-cosEvent usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles erlang-cosEventDomain usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles erlang-cosFileTransfer usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles erlang-cosNotification usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles erlang-cosProperty usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles erlang-cosTime usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles erlang-cosTransactions usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles erlang-ic usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles erlang-orber usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{with doc}
%files -f %{oreon_filedir}/main.list
%files -n erlang-corba-doc -f %{oreon_filedir}/erlang-corba-doc.list
%files -n erlang-cosEvent -f %{oreon_filedir}/erlang-cosEvent.list
%files -n erlang-cosEventDomain -f %{oreon_filedir}/erlang-cosEventDomain.list
%files -n erlang-cosFileTransfer -f %{oreon_filedir}/erlang-cosFileTransfer.list
%files -n erlang-cosNotification -f %{oreon_filedir}/erlang-cosNotification.list
%files -n erlang-cosProperty -f %{oreon_filedir}/erlang-cosProperty.list
%files -n erlang-cosTime -f %{oreon_filedir}/erlang-cosTime.list
%files -n erlang-cosTransactions -f %{oreon_filedir}/erlang-cosTransactions.list
%files -n erlang-ic -f %{oreon_filedir}/erlang-ic.list
%files -n erlang-orber -f %{oreon_filedir}/erlang-orber.list

%changelog

%autochangelog
%endif
