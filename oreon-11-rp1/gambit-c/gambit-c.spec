%global source0_hash 0ec19b755dbda6c540e9e60b7235d801f26f40c2f211ddfb729b756218bcc873
Name:           gambit-c
Version:        4.9.8
Release:        1%{?dist}
Summary:        Scheme programming system
License:        Apache-2.0 OR LGPL-2.1-only
URL:            http://gambitscheme.org/
%global _dirname gambit-v%(echo %{version} | sed -e 's/\\./_/g')-devel
Source0:        https://github.com/gambit/gambit/archive/v%{version}/gambit-%{version}.tar.gz
Source1:        gambit-init.el
Patch0:         gambc-v4_2_8-modtime.patch
Requires:       gcc
Requires:       emacs-filesystem >= %{_emacs_version}
# oreon:deps
BuildRequires:  emacs
BuildRequires:  gcc
BuildRequires:  make
# /oreon:deps
%description
Gambit-C includes a Scheme interpreter and a Scheme compiler which can
be used to build standalone executables.  Because the compiler
generates portable C code it is fairly easy to port to any platform
with a decent C compiler.

The Gambit-C system conforms to the R4RS, R5RS and IEEE Scheme
standards.  The full numeric tower is implemented, including: infinite
precision integers (bignums), rationals, inexact reals (floating point
numbers), and complex numbers.

%package        doc
Summary:        Documentation for %{name}
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Obsoletes:      gambit-c-doc < %{version}-%{release}
%description    doc
Gambit-C includes a Scheme interpreter and a Scheme compiler which can
be used to build standalone executables.  Because the compiler
generates portable C code it is fairly easy to port to any platform
with a decent C compiler.

This package contains the Gambit-C user manual in HTML and PDF formats.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n gambit-%{version} -p1
#-n %{_dirname} -p1
# Gambit tries to do a git update-index if a git repo is detected
rm -rf .git

# Permission fixes
chmod -x lib/*.{c,h}

%build

%ifnarch ppc64le
%configure --enable-trust-c-tco \
           --enable-dynamic-clib \
           --enable-single-host \
	   --bindir=%{_libdir}/%{name}/bin \
           --libdir=%{_libdir}/%{name}
%else
%configure --enable-dynamic-clib \
           --enable-single-host \
           --bindir=%{_libdir}/%{name}/bin \
           --libdir=%{_libdir}/%{name}
%endif
make %{?_smp_mflags}
(cd misc && %{_emacs_bytecompile} gambit.el)
%check

make check
%install
make install DESTDIR=$RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}
for i in gsc gsi
do
  ln -sf ../%{_lib}/%{name}/bin/$i $RPM_BUILD_ROOT%{_bindir}/$i
done
cat > $RPM_BUILD_ROOT%{_bindir}/gsix <<EOF
%{_libdir}/%{name}/bin/six $@
EOF
chmod +x $RPM_BUILD_ROOT%{_bindir}/gsix
rm -rf $RPM_BUILD_ROOT%{_prefix}/doc
mkdir -p $RPM_BUILD_ROOT%{_emacs_sitestartdir}
cp -p misc/gambit.elc $RPM_BUILD_ROOT%{_emacs_sitelispdir}
cp -p %{SOURCE1} $RPM_BUILD_ROOT%{_emacs_sitestartdir}
(cd $RPM_BUILD_ROOT%{_libdir} && ln -s %{name}/*.a .)
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n gambit-c-doc -f %{oreon_filedir}/gambit-c-doc.list

%changelog

%autochangelog
