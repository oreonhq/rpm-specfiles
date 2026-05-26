%{!?postgresql_default:%global postgresql_default 0}

%global pname vector
%global sname pgvector
%global pgversion 16

%ifarch ppc64 ppc64le s390 s390x armv7hl
	%{!?llvm:%global llvm 0}
%else
	%{!?llvm:%global llvm 0}
%endif

Name:		postgresql%{pgversion}-%{sname}
Version:	0.6.2
Release:	7%{?dist}
Summary:	Open-source vector similarity search for Postgres
License:	PostgreSQL
URL:		https://github.com/%{sname}/%{sname}/
Source0:	https://github.com/%{sname}/%{sname}/archive/refs/tags/v%{version}.tar.gz
# oreon url source checksums begin
%global source0_sha256 a11cc249a9f3f3d7b13069a1696f2915ac28991a72d7ba4e2bcfdceddbaeae49
%global source0_file v0.6.2.tar.gz
# oreon url source checksums end

%if %?postgresql_default
%global pkgname %{sname}
%package -n %{pkgname}
Summary: Open-source vector similarity search for Postgres
%else
%global pkgname %name
%endif

BuildRequires:	make gcc
BuildRequires:	postgresql%{pgversion}-server-devel
Requires:	postgresql%{pgversion}-server

%global precise_version %{?epoch:%epoch:}%version-%release

%if %?postgresql_default
Provides: postgresql-%{sname} = %precise_version
Provides: %name = %precise_version
%endif
Provides: %{pkgname}%{?_isa} = %precise_version
Provides: %{pkgname} = %precise_version
Provides: %{sname}-any
Conflicts: %{sname}-any

%description
Open-source vector similarity search for Postgres. Supports L2 distance,
inner product, and cosine distance

%description -n %{pkgname}
Open-source vector similarity search for Postgres. Supports L2 distance,
inner product, and cosine distance

%if %llvm
%package -n %{pkgname}-llvmjit
Summary:	Just-in-time compilation support for pgvector
Requires:	%{pkgname}%{?_isa} = %precise_version
Requires:	llvm => 13.0

%description -n %{pkgname}-llvmjit
This packages provides JIT support for pgvector
%endif

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/v0.6.2.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "a11cc249a9f3f3d7b13069a1696f2915ac28991a72d7ba4e2bcfdceddbaeae49" || { echo "oreon: Source0 SHA256 mismatch for v0.6.2.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q -n %{sname}-%{version}

%build
%make_build %{?_smp_mflags} OPTFLAGS=""

%install
%make_install

#Remove header file, we don't need it right now:
%{__rm} %{buildroot}/%{_includedir}/pgsql/server/extension/%{pname}/%{pname}.h

%files -n %{pkgname}
%doc README.md
%license LICENSE
%{_libdir}/pgsql/%{pname}.so
%{_datadir}/pgsql/extension//%{pname}.control
%{_datadir}/pgsql/extension/%{pname}*sql
%if %llvm
%files -n %{pkgname}-llvmjit
%{_libdir}/pgsql/bitcode/%{pname}*.bc
%{_libdir}/pgsql/bitcode/%{pname}/src/*.bc
%endif

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.6.2-7
- Import
