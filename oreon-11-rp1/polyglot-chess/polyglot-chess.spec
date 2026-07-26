%global source0_hash 679334a4cbc604783d051d8e52a6ba2863eb9cc135dae48cf4c191452840bcb2

%global _vpath_srcdir src
%undefine __cmake_in_source_build

%global srcname     polyglot
%global commitdate  20140902
%global commit0     f46ee068860d363ace27004ec4da588bf4b48147

Name:           %{srcname}-chess
Version:        1.4
Release:        31.%{commitdate}git%(c=%{commit0}; echo ${c:0:7})%{?dist}
Summary:        Polyglot chess opening book program

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://github.com/sshivaji/%{srcname}
Source0:        %{url}/archive/%{commit0}.tar.gz#/%{srcname}-%{commit0}.tar.gz

# cmake https://github.com/sshivaji/polyglot/issues/2
Source1:        %{srcname}-CMakeLists.txt
# community provides some nice addons
Source2:        https://launchpadlibrarian.net/4993987/%{srcname}_1.4-2.diff.gz

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  pkgconfig(leveldb)

%description
PolyGlot is a "UCI adapter". It connects a UCI chess engine to an
xboard interface such as WinBoard. UCI2WB is another such adapter
(for Windows).
PolyGlot tries to solve known problems with other adapters. For
instance, it detects and reports draws by fifty-move rule, repetition,
etc ...

New Features: Builds a polyglot book but supports a leveldb position/game
index as well. The leveldb option can be enabled with -leveldb 
 

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qn%{srcname}-%{commit0}
zcat %{SOURCE2} |patch -p1
# use proper Fedora flags
rm src/Makefile
cp %{SOURCE1} src/CMakeLists.txt
# W: wrong-file-end-of-line-encoding
sed -i 's,\r$,,' readme.txt debian/example-files/*
# rename binary
sed 's,%{srcname},%{name},' debian/%{srcname}.6 >%{name}.6
sed -i 's,%{srcname},%{name},' src/CMakeLists.txt

%build
# TODO: Please submit an issue to upstream (rhbz#2381371)
export CMAKE_POLICY_VERSION_MINIMUM=3.5
%cmake
%cmake_build

%install
# W: unstripped-binary-or-object
install -p -m0755 %{_vpath_builddir}/%{name} -D %{buildroot}%{_bindir}/%{name}
# W: spurious-executable-perm
install -p -m0644 %{name}.6 -D %{buildroot}%{_mandir}/man6/%{name}.6

%files
%license LICENSE
%doc readme.txt README.md
%doc debian/*.Debian debian/example-files/
%{_mandir}/man*/%{name}*
%{_bindir}/%{name}

%changelog
%autochangelog
