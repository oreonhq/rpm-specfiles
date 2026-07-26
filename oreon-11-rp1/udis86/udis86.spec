%global source0_hash 5baecc8a4a15df4494817f8c50c956a53b8e164b17262cfe16072a01308e4266

%global gitrev 56ff6c8

Name:           udis86
Version:        1.7.2
Release:        30.%{gitrev}%{?dist}
Summary:        A disassembler library for x86 and x86-64

License:        BSD-2-Clause
URL:            https://github.com/vmt/udis86
Source0:        %{name}-%{gitrev}.tar.xz
Patch0:         udis86-ud_opcode.patch
Patch1:         udis86-symresolve.patch
Patch2:         udis86-ax_prog_sphinx_version.patch
Patch3:         udis86-docs_manual_Makefile.am.patch

BuildRequires:  make
BuildRequires:  libtool
BuildRequires:  python
BuildRequires:  python3-sphinx

%description
udis86 is a disassembler library (libudis86) for x86 and x86-64.
The primary intent is to aid binary code analysis.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{gitrev}
%patch -P0 -p1 -b .ud_opcode
%patch -P1 -p1 -b .symresolve
%patch -P2 -p1 -b .origm4
%patch -P3 -p1 -b .automake
find '(' -name '*.c' -or -name '*.h' ')' -exec chmod 644 {} \;

%build
./autogen.sh
%configure --disable-static \
           --enable-shared \
           --disable-silent-rules \
           --with-python=%{_bindir}/python3 \
           --without-yasm \
           --with-sphinx-build=%{_bindir}/sphinx-build-3
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make %{?_smp_mflags}
make -C docs/manual html-local

%install
make install DESTDIR=%{buildroot}
find %{buildroot} -name '*.la' -exec rm -f {} ';'
# udis86 overrides "docdir" from automake to datadir/docs
rm -rf %{buildroot}%{_datadir}/docs
rm -rf %{buildroot}%{_docdir}

%ldconfig_scriptlets

%files
%{_bindir}/udcli
%{_libdir}/*.so.*

%files devel
%doc docs/x86/optable.* docs/manual/html/*.html docs/manual/html/_static
%{_includedir}/*
%{_libdir}/*.so

%changelog
%autochangelog
