%global source0_hash f5a6539059cf5e597dbeda37bfa4874b1e8dea063c8d93bf85a2b44af90a5bd4
%bcond_without check
Name:           libarchive
Version:        3.8.9
Release:        1%{?dist}
Summary:        A library for handling streaming archive formats
License:        BSD-2-Clause AND FSFULLR AND GPL-2.0-or-later WITH Libtool-exception AND BSD-3-Clause AND FSFUL
URL:            https://www.libarchive.org/
Source0:        https://libarchive.org/downloads/%{name}-%{version}.tar.gz
Patch0001: 0001-Drop-rmd160-from-OpenSSL.patch
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  bzip2-devel
BuildRequires:  e2fsprogs-devel
BuildRequires:  gcc
BuildRequires:  libacl-devel
BuildRequires:  libattr-devel
BuildRequires:  libtool
BuildRequires:  libxml2-devel
BuildRequires:  libzstd-devel
BuildRequires:  lz4-devel
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  xz-devel
BuildRequires:  zlib-devel
# /oreon:deps
%description
Libarchive is a programming library that can create and read several different
streaming archive formats, including most popular tar variants, several cpio
formats, and both BSD and GNU ar variants. It can also write shar archives and
read ISO9660 CDROM images and ZIP archives.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package -n bsdtar
Summary:        Manipulate tape archives
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description -n bsdtar
The bsdtar package contains standalone bsdtar utility split off regular
libarchive packages.

%package -n bsdcpio
Summary:        Copy files to and from archives
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description -n bsdcpio
The bsdcpio package contains standalone bsdcpio utility split off regular
libarchive packages.

%package -n bsdcat
Summary:        Expand files to standard output
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description -n bsdcat
The bsdcat program typically takes a filename as an argument or reads standard
input when used in a pipe.  In both cases decompressed data it written to
standard output.

%package -n bsdunzip
Summary:        Extract files from a ZIP archive
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description -n bsdunzip
The bsdunzip package contains standalone bsdunzip utility split off regular
libarchive packages. It is designed to provide an interface compatible with Info-ZIP's.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

autoreconf -ifv
%configure --disable-static LT_SYS_LIBRARY_PATH=%_libdir
%make_build
%install
%make_install
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
replace ()
{
    filename=$1
    file=`basename "$filename"`
    binary=${file%%.*}
    pattern=${binary##bsd}
    awk "
        /^.Dt ${pattern^^} 1/ {
            print \".Dt ${binary^^} 1\";
            next;
        }
        !stop && /^.Nm $pattern/ {
            print \".Nm $binary\" ;
            stop = 1 ;
            next;
        }
        1;
    " "$filename" > "$filename.new"
    mv "$filename".new "$filename"
}
for manpage in bsdtar.1 bsdcpio.1
do
    installed_manpage=`find "$RPM_BUILD_ROOT" -name "$manpage"`
    replace "$installed_manpage"
done
%oreon_autofiles bsdtar usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles bsdcpio usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles bsdcat usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles bsdunzip usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%if %{with check}
logfiles ()
{
    find -name '*_test.log' -or -name test-suite.log
}
tempdirs ()
{
    cat `logfiles` \
        | awk "match(\$0, /[^[:space:]]*`date -I`[^[:space:]]*/) { print substr(\$0, RSTART, RLENGTH); }" \
        | sort | uniq
}
cat_logs ()
{
    for i in `logfiles`
    do
        echo "=== $i ==="
        cat "$i"
    done
}
run_testsuite ()
{
    rc=0
    %make_build check -j1 || {
        cat_logs
        for i in `tempdirs`; do
            if test -d "$i" ; then
                find $i -printf "%p\n    ~> a: %a\n    ~> c: %c\n    ~> t: %t\n    ~> %s B\n"
                cat $i/*.log
            fi
        done
        return 1
    }
    cat_logs
}
%ifarch ppc
run_testsuite || run_testsuite
%else
run_testsuite
%endif
%endif
%files -f %{oreon_filedir}/main.list
%files -n libarchive-devel -f %{oreon_filedir}/libarchive-devel.list
%files -n bsdtar -f %{oreon_filedir}/bsdtar.list
%files -n bsdcpio -f %{oreon_filedir}/bsdcpio.list
%files -n bsdcat -f %{oreon_filedir}/bsdcat.list
%files -n bsdunzip -f %{oreon_filedir}/bsdunzip.list

%changelog

%autochangelog
