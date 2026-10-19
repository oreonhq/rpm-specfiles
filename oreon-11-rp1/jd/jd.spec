%global source0_hash 32d2f8c5debba8928435adda325ceb2e3da019f0c2b21b7a7a042d5629848200
%undefine       _changelog_trimtime
%define         main_ver      0.16.0
%dnl %define         pre_ver       alpha
%global         reponame      JDim
%global         gitdate       20260316
%global         gitcommit     cc9878799dc5f5b5351516944291e77d2425cc4e
%dnl %global         gitcommit     JDim-v%{main_ver}
%global         shortcommit   %(c=%{gitcommit}; echo ${c:0:7})
%global         tarballdate   20260317
%global         tarballtime   0903
%define         extra_rel     %{nil}
%define         use_gitcommit_as_rel  0
%define         vendorname    fedora
%define         fontpackage   mona-fonts-VLGothic
%if 0%{?use_gitcommit_as_rel} >= 1
%global         gittag        %{gitdate}git%{shortcommit}
%global         gitver_rpm    ^%{gittag}
%global         gitver_build  -%{gittag}
%else
%global         gittag        %{nil}
%global         gitver_rpm    %{nil}
%global         gitver_build  %{nil}
%endif
%define         _with_migemo  1
%define         migemo_dict   %{_datadir}/cmigemo/utf-8/migemo-dict
%global		use_gcc_strict_sanitize	0
%global		flagrel	%{nil}
%if	0%{?use_cppcheck} >= 1
%global		flagrel	%{flagrel}.cppcheck
%endif
%if	0%{?use_gcc_strict_sanitize} >= 1
%global		flagrel	%{flagrel}.san
%endif
%if 0%{?use_gitcommit_as_rel} >= 1
%global		clamp_mtime_to_source_date_epoch	0
%endif
Name:           jd
Epoch:          1
Version:        %{main_ver}%{?strtag:.%{strtag}}%{?pre_ver:~%{pre_ver}}%{gitver_rpm}
Release:        1%{?dist}
Summary:        A 2ch browser
License:        GPL-2.0-only
URL:            https://github.com/JDimproved/JDim
%dnl Source0:        http://dl.sourceforge.jp/jd4linux/%{repoid}/%{name}-%{main_ver}-%{strtag}.tgz
Source0:        %{reponame}-%{tarballdate}T%{tarballtime}.tar.gz
Source1:        create-JD-git-bare-tarball.sh
%if 0%{?_with_migemo} >= 1
%endif
%if 0%{?use_gcc_strict_sanitize}
%endif
Requires:       %{fontpackage}
# oreon:deps
BuildRequires:  //bin/appstream-util
BuildRequires:  //bin/desktop-file-validate
BuildRequires:  cmigemo-devel
BuildRequires:  gcc-c++
BuildRequires:  git
BuildRequires:  gtest-devel
BuildRequires:  libgcrypt-devel
BuildRequires:  libxcrypt-devel
BuildRequires:  make
BuildRequires:  meson
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(gnutls)
BuildRequires:  pkgconfig(gtkmm-3.0)
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(sm)
# /oreon:deps
%description
JD is a 2ch browser based on gtkmm2.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -c -T -n %{name}-%{main_ver}%{?strtag:.%{strtag}}%{gitver_build} -a 0

git clone ./%{reponame}.git
cd JDim

git config user.name "%{name} Fedora maintainer"
git config user.email "%{name}-maintainers@fedoraproject.org"

%if 0%{?use_gitcommit_as_rel} >= 1
git checkout -b %{main_ver}-fedora-local %{gitcommit}
%else
git checkout -b %{main_ver}-fedora-local %{gitcommit}
#git checkout -b %{main_ver}-fedora-local %{reponame}-v%{main_ver}
%endif

cp -a [A-Z]* ..

# reset to base, as git information is embedded in the source
git checkout -b %{main_ver}-fedora
#git reset %{reponame}-v%{main_ver}
%if 0%{?use_gitcommit_as_rel} >= 1
git reset %{gitcommit}
%else
git reset %{gitcommit}
#git reset %{reponame}-v%{main_ver}
%endif

%build

cd %{reponame}
export TZ='Asia/Tokyo'
%set_build_flags
export LDFLAGS="$LDFLAGS -Wl,--push-state,--no-as-needed -lcrypt -Wl,--pop-state"
%if 0%{?use_gcc_strict_sanitize}
export CC="${CC} -fsanitize=address -fsanitize=undefined"
export CXX="${CXX} -fsanitize=address -fsanitize=undefined"
export LDFLAGS="${LDFLAGS} -pthread"
%endif
%meson \
    -Dalsa=enabled \
    -Dbuild_tests=enabled \
    -Dcompat_cache_dir=enabled \
%if 0%{?_with_migemo} >= 1
    -Dmigemo=enabled \
    -Dmigemodict=%{migemo_dict} \
%endif
    -Dpackager="jd-%{version}-%{release}.%{_arch}.rpm by Fedora Project" \
    -Dtls=gnutls \
    %{nil}
%meson_build \
	--ninja-args "-k 0"
%install
cd %{reponame}
%meson_install
ln -sf jdim %{buildroot}%{_bindir}/%{name}
ln -sf jdim.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop
%oreon_autofiles main

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/jdim.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/jdim.metainfo.xml
cd %{reponame}
%if 0%{?use_gcc_strict_sanitize} >= 1
export ASAN_OPTIONS=detect_leaks=0
%endif
%meson_test -v
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
