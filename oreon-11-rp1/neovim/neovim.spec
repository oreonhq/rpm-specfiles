%global source0_hash a810c95332317bd0017e1ca07e376a8472c79075cbed00fa3737d190a8a0a45a
%global source3_hash none
%bcond_with jemalloc
%ifarch %{arm} %{ix86} x86_64 %{mips} s390x
  %bcond_without luajit
%else
  %ifarch aarch64
    %bcond_without luajit
  %else
    %bcond_with luajit
  %endif
%endif
%if 0%{?el10} || (0%{?oreon} >= 11)
%bcond_without system_treesitter
%else
%bcond_with system_treesitter
%endif
%global luv_min_ver 1.43.0
%if %{with system_treesitter}
%global tree_sitter_min_ver 0.26.7
%endif
%global vterm_min_ver 0.3.3
%global luv_include_dir %{_includedir}/luv
%if %{with luajit}
%global luajit_version 2.1
%global lua_prg %{_bindir}/luajit
%else
%global lua_version 5.1
%global lua_prg %{_bindir}/lua-5.1
%endif
Name:           neovim
Version:        0.12.5
Release:        1%{?dist}
License:        Apache-2.0 AND Vim AND MIT
Summary:        Vim-fork focused on extensibility and agility
Url:            https://neovim.io
Source0:        https://github.com/neovim/neovim/archive/refs/tags/v%{version}.tar.gz#/neovim-%{version}.tar.gz
Source1:        sysinit.vim
Source2:        nvim-user-template.in
Source4:        neovim-bundled-licenses.txt
Patch1000:        neovim-lua-bit32.patch
%if %{with luajit}
Requires:       luajit2.1-luv >= %{luv_min_ver}
%else
Requires:       lua5.1-luv >= %{luv_min_ver}
%endif
Requires:       lua5.1-lpeg >= 1.1.0
%if %{with jemalloc}
%endif
Requires:       libvterm >= %{vterm_min_ver}
%if %{with system_treesitter}
Requires:       libtree-sitter >= %{tree_sitter_min_ver}
%endif
Recommends:     tree-sitter-cli
Suggests:       (python2-neovim if python2)
Suggests:       (python3-neovim if python3)
Recommends:     xsel
Recommends:     wl-clipboard
Recommends:     ripgrep
Recommends:     inotify-tools
# oreon:deps
BuildRequires:  cmake
BuildRequires:  compat-lua
BuildRequires:  compat-lua-devel
BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  gperf
BuildRequires:  libluv-devel
BuildRequires:  lua5.1-bit32
BuildRequires:  lua5.1-lpeg
BuildRequires:  lua5.1-mpack
BuildRequires:  msgpack-devel
BuildRequires:  ninja-build
BuildRequires:  pkgconfig(libutf8proc)
BuildRequires:  pkgconfig(libuv)
BuildRequires:  pkgconfig(termkey)
BuildRequires:  pkgconfig(unibilium)
BuildRequires:  pkgconfig(vterm)
# /oreon:deps
%description
Neovim is a refactor - and sometimes redactor - in the tradition of
Vim, which itself derives from Stevie. It is not a rewrite, but a
continuation and extension of Vim. Many rewrites, clones, emulators
and imitators exist; some are very clever, but none are Vim. Neovim
strives to be a superset of Vim, notwithstanding some intentionally
removed misfeatures; excepting those few and carefully-considered
excisions, Neovim is Vim. It is built for users who want the good
parts of Vim, without compromise, and more.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | cut -d' ' -f1); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q
vdir="%{name}-%{version}-vendor"
mkdir -p _vbuild && pushd _vbuild
cmake -S ../cmake.deps -B deps -G Ninja -DUSE_BUNDLED=OFF -DUSE_BUNDLED_TS=ON -DUSE_BUNDLED_TS_PARSERS=ON
readarray -t _vt < <(basename -a deps/build/downloads/treesitter* | xargs -I {} echo build/src/{}-stamp/{}-download)
ninja -C deps "${_vt[@]}"
mkdir -p "../${vdir}"
cp -a deps/build/downloads/. "../${vdir}/"
popd

cp %{SOURCE4} .

%if %{without luajit}
%patch -P 1000 -p1
%endif

%build

HOSTNAME=koji
USERNAME=koji
mkdir -p .deps/build/
ln -sfr ../%{name}-%{version}-vendor .deps/build/downloads
%define _vpath_srcdir cmake.deps
%define __cmake_builddir .deps
%cmake -DCMAKE_POLICY_VERSION_MINIMUM=3.5 -DCMAKE_BUILD_TYPE=RelWithDebInfo \
       -DUSE_BUNDLED=OFF \
%if %{without system_treesitter}
       -DUSE_BUNDLED_TS=ON \
%endif
       -DUSE_BUNDLED_TS_PARSERS=ON
%cmake_build
%define _vpath_srcdir .
%define __cmake_builddir redhat-linux-build
%cmake -DCMAKE_POLICY_VERSION_MINIMUM=3.5 -DCMAKE_BUILD_TYPE=RelWithDebInfo \
       -DPREFER_LUA=%{?with_luajit:OFF}%{!?with_luajit:ON} \
       -DLUA_PRG=%{lua_prg} \
       -DENABLE_JEMALLOC=%{?with_jemalloc:ON}%{!?with_jemalloc:OFF} \
       -DLIBLUV_INCLUDE_DIR:PATH=%{luv_include_dir} \
       -DENABLE_TRANSLATIONS=ON
%cmake_build
%install
%cmake_install
install -p -m 644 %{SOURCE1} %{buildroot}%{_datadir}/nvim/sysinit.vim
install -p -m 644 %{SOURCE2} %{buildroot}%{_datadir}/nvim/template.spec
desktop-file-install --dir=%{buildroot}%{_datadir}/applications \
    runtime/nvim.desktop
install -d -m0755 %{buildroot}%{_datadir}/pixmaps
install -m0644 runtime/nvim.png %{buildroot}%{_datadir}/pixmaps/nvim.png
%fdupes %{buildroot}%{_datadir}/
find %{buildroot}%{_datadir} \( -name "*.bat" -o -name "*.awk" \) \
    -print -exec chmod -x '{}' \;
%find_lang nvim
%transfiletriggerin -- %{_datadir}/nvim/runtime/doc
NVIM_LOG_FILE=/dev/null %{_bindir}/nvim -u NONE -es -c ":helptags %{_datadir}/nvim/runtime/doc" -c ":q" &> /dev/null || :
%transfiletriggerpostun -- %{_datadir}/nvim/runtime/doc
> %{_datadir}/nvim/runtime/doc/tags || :
NVIM_LOG_FILE=/dev/null %{_bindir}/nvim -u NONE -es -c ":helptags %{_datadir}/nvim/runtime/doc" -c ":q" &> /dev/null || :
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.12.2-1
- Import
