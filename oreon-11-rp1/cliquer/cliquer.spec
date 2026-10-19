%global source3_hash be27c2bbd91b3bb7adec00acf322674dd6ce6bae2ddf80c621fd81247fa7f6eb
%global source2_hash c91e6077cbbbd68e30d99a811d3f89a22db621410c578b6419eb8cb7d7401026
%global source1_hash ec72e5dc199a7a7e97371f343bd1219bd4bbcc2d44a3f4d93b50b298c9ba7da2
%global source0_hash c1d7cc927b7efe76ff4f11e1f01bee473e37360fb54843b16b287e3ad161287b
Name:           cliquer
Version:        1.23
Release:        1%{?dist}
Summary:        Find cliques in arbitrary weighted graphs
License:        GPL-2.0-or-later
URL:            https://users.aalto.fi/~pat/cliquer.html
Source0:        https://github.com/dimpase/autocliquer/releases/download/v%{version}/%{name}-%{version}.tar.gz
Source1:        http://users.aalto.fi/~pat/%{name}/%{name}_fm.pdf
Source2:        http://users.aalto.fi/~pat/%{name}/%{name}.pdf
Source3:        http://users.aalto.fi/~pat/%{name}/%{name}_bm.pdf
Source4:        %{name}.1
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
# /oreon:deps
%description
The main cliquer package contains a command-line interface to the cliquer
library.  Note that the upstream binary name is "cl", which is too generic for
Fedora.  Therefore, the binary is named "cliquer".

%package libs
Summary:        Library to find cliques in arbitrary weighted graphs
%description libs
Cliquer is a set of C routines for finding cliques in an arbitrary weighted
graph.  It uses an exact branch-and-bound algorithm developed by Patric
Östergård.  It is designed with the aim of being efficient while still being
flexible and easy to use.

%package devel
Summary:        Development files for cliquer
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
%description devel
Development files for cliquer.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
cp -p %{SOURCE1} %{SOURCE2} %{SOURCE3} .

%conf
sed -i \
    's/59 Temple Place, Suite 330, Boston, MA  02111-1307/51 Franklin Street, Suite 500, Boston, MA  02110-1335/' \
    COPYING

%build

%configure --disable-static --disable-silent-rules
sed -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    -e 's|CC="\(.*g..\)"|CC="\1 -Wl,--as-needed"|' \
    -i libtool
%make_build
%install
%make_install
chmod 0755 %{buildroot}%{_libdir}/libcliquer.so.1.*
rm -fr %{buildroot}%{_datadir}/%{name}
mv %{buildroot}%{_bindir}/cl %{buildroot}%{_bindir}/%{name}
mkdir -p %{buildroot}%{_mandir}/man1
cp -p %{SOURCE4} %{buildroot}%{_mandir}/man1
%oreon_autofiles cliquer-libs usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles cliquer-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

LD_LIBRARY_PATH=$PWD make test
%files -f %{oreon_filedir}/main.list
%files -n cliquer-libs -f %{oreon_filedir}/cliquer-libs.list
%files -n cliquer-devel -f %{oreon_filedir}/cliquer-devel.list

%changelog

%autochangelog
