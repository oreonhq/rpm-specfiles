%global source0_hash none
%bcond check 0
%global debug_package %{nil}
%global goipath         modernc.org/ccorpus2
%global forgeurl        https://gitlab.com/cznic/ccorpus2
Version:                1.5.1
%global tag             v%{version}
%gometa -f
%global common_description %{expand:
Continuation of ccorpus but using embed.FS.}
%global golicenses      LICENSE \\\
                        LICENSE-benchmarksgame \\\
                        LICENSE-c9x \\\
                        COPYING-redis \\\
                        COPYING.LESSER-mpc \\\
                        COPYING-pcre \\\
                        COPYING-pcre2 \\\
                        COPYING-pcre2 \\\
                        LICENSE-quickjs \\\
                        LICENSE-cxgo \\\
                        LICENSE-zlib \\\
                        LICENSE-mir \\\
                        COPYRIGHT-postgresql \\\
                        COPYING-gmp \\\
                        COPYRIGHT-musl-1.2.2 \\\
                        license.terms-tcl \\\
                        LICENSE-tcc \\\
                        COPYING-hdf5 \\\
                        COPYING_LBNL_HDF5-hdf5 \\\
                        COPYING-mpfr \\\
                        COPYING.LESSER-mpfr \\\
                        LICENSE-cxgo \\\
                        COPYING3-gcc
%global godocs          AUTHORS CONTRIBUTORS README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Continuation of ccorpus but using embed.FS
License:        BSD-3-Clause AND blessing AND GPL-3.0-or-later AND LGPL-3.0-only AND MIT AND TCL AND Zlib
URL:            %{gourl}
Source0:        %{forgeurl}/-/archive/%{tag}/ccorpus2-%{tag}.tar.bz2
Source1:        assets.go
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description %{common_description}

%prep

%goprep
%autopatch -p1
# Not free:
rm -rfv assets/CompCert-3.6 assets/github.com/AbsInt/CompCert
# Gather asset licenses:
pushd assets
mv benchmarksgame-team.pages.debian.net/LICENSE ../LICENSE-benchmarksgame
tar xvf c9x.me/git/qbe.tar.gz
mv qbe/LICENSE ../LICENSE-c9x
# ccgo is BSD-3-Clause.
tar xvf download.redis.io/releases/redis-6.2.6.tar.gz
mv redis-6.2.6/COPYING ../COPYING-redis
tar xvf ftp.gnu.org/gnu/mpc/mpc-1.2.1.tar.gz
mv mpc-1.2.1/COPYING.LESSER ../COPYING.LESSER-mpc
tar xvf ftp.pcre.org/pub/pcre.tar.gz
mv pcre/COPYING ../COPYING-pcre
tar xvf ftp.pcre.org/pub/pcre2.tar.gz
mv pcre2/COPYING ../COPYING-pcre2
tar xvf github.com/bellard/quickjs/archive/refs/heads/quickjs-master/quickjs-master.tar.gz
mv quickjs-master/LICENSE ../LICENSE-quickjs
mv github.com/cxgo/LICENSE ../LICENSE-cxgo
# github.com/freebsd is BSD.
mv github.com/gcc-mirror/gcc/COPYING3 ../COPYING3-gcc
tar xvf github.com/git/git/archive/refs/tags/v2.35.1.tar.gz
mv git-2.35.1/COPYING COPYING-git
# github.com/IIJ-NetBSD is BSD.
tar xvf github.com/madler/zlib.tar.gz
sed -n '/^Copyright notice:/,$p' zlib/README >../LICENSE-zlib
# github.com/openbsd is BSD.
mv github.com/vnmakarov/mir/LICENSE ../LICENSE-mir
tar xvf git.postgresql.org/git/postgresql.tar.gz
mv postgresql/COPYRIGHT ../COPYRIGHT-postgresql
tar xvf gmplib.org/download/gmp/gmp-6.2.1.tar.gz
mv gmp-6.2.1/COPYING ../COPYING-gmp
tar xvf musl.libc.org/releases/musl-1.2.2.tar.gz
mv musl-1.2.2/COPYRIGHT ../COPYRIGHT-musl-1.2.2
tar xvf musl.libc.org/releases/musl-1.2.4.tar.gz
mv musl-1.2.4/COPYRIGHT ../COPYRIGHT-musl-1.2.4
tar xvf sourceforge.net/projects/tcl/files/Tcl/tcl.tar.gz
mv tcl/license.terms ../license.terms-tcl
# sqlite-amalgamation is public domain.
# sqlite-amalgamation-3380100 is public domain.
mv tcc-0.9.27/tests/tests2/LICENSE ../LICENSE-tcc
tar xvf www.hdfgroup.org/downloads/hdf5/source-code/hdf5-1.12.1.tar.gz
mv hdf5-1.12.1/COPYING ../COPYING-hdf5
mv hdf5-1.12.1/COPYING_LBNL_HDF5 ../COPYING_LBNL_HDF5-hdf5
# www.lua.org is MIT.
tar xvf www.mpfr.org/mpfr-current/mpfr-4.1.0.tar.gz
mv mpfr-4.1.0/COPYING ../COPYING-mpfr
mv mpfr-4.1.0/COPYING.LESSER ../COPYING.LESSER-mpfr
popd
cp %{S:1} .

%install
%gopkginstall
%oreon_autofiles main
%if %{with check}
%check

%gocheck -d .
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
