%global source0_hash 9f23d6f6871cc0c8b568757b99468c23dd8126d086e5a46f66923d46f6c7fa33
%bcond html_docs 1
Name:           gn
%global commit 2941d2a26fa9cef3103f10e1dee5da7cd404008a
%global access 20260314
%global shortcommit %{sub %{commit} 1 12}
%global position 2345
Version:        %{position}^%{access}.%{shortcommit}
Release:        1%{?dist}
Summary:        Meta-build system that generates build files for Ninja
License:        BSD-3-Clause AND Unicode-DFS-2016 AND ICU
SourceLicense:  %{license} AND Apache-2.0
URL:            https://gn.googlesource.com/gn
Source0:        https://%{name}.googlesource.com/%{name}/+archive/%{commit}.tar.gz#/%{name}-2941d2a26fa9.tar.gz
Source1:        last_commit_position.h
Source2:        update-version
Patch:          0001-Downstream-only-do-not-override-optimization-flags.patch
Patch:          0002-Downstream-only-do-not-build-with-Wno-format.patch
ExcludeArch:    %{ix86}
%if %{with html_docs}
%endif
Requires:       vim-filesystem
Requires:       python3
Provides:       vim-gn = %{version}-%{release}
Requires:       emacs-filesystem >= %{_emacs_version}
Provides:       emacs-gn = %{version}-%{release}
Provides:       bundled(icu) = 60
# oreon:deps
BuildRequires:  emacs-common
BuildRequires:  gcc-c++
BuildRequires:  help2man
BuildRequires:  ninja-build
BuildRequires:  pandoc
BuildRequires:  parallel
BuildRequires:  python3-devel
# /oreon:deps
%description
GN is a meta-build system that generates build files for Ninja.

%package doc
Summary:        Documentation for GN
BuildArch:      noarch
%description doc
The gn-doc package contains detailed documentation for GN.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -c -n gn-%{commit} -p1

# Use pre-generated last_commit_position.h.
mkdir -p ./out
cp -vp '%{SOURCE1}' ./out

# Copy and rename vim extensions readme for use in the main documentation
# directory.
cp -vp misc/vim/README.md README-vim.md

# Fix shebangs in examples and such.
%py3_shebang_fix .

%conf
AR='gcc-ar'; export AR
# Treating warnings as errors is too strict for downstream builds.
#
# Both --use-icf and --use-lto add compiler flags that only work with clang++,
# not with g++. We do get LTO on Fedora anyway, since we respect the
# distribution’s build flags.
%{python3} build/gen.py \
    --allow-warnings \
    --no-last-commit-position \
    --no-strip \
    --no-static-libstdc++

%build

ninja -j %{_smp_build_ncpus} -C out -v
%if %{with html_docs}
find . -type f -name '*.md' | parallel -v pandoc -o '{.}.html' '{}'
%endif
help2man \
    --name='%{summary}' \
    --version-string="gn $(./out/gn --version)" \
    --no-info \
    ./out/gn |
  tr -d '\302\240' |
  sed -r -e 's/(^[[:alnum:]_]+:)/.TP\n.B \1\n/' \
      -e 's/\[([^]]+)\]/\\fI[\1]\\fR/g' > out/gn.1
%install
install -t '%{buildroot}%{_bindir}' -D -p out/gn
install -d '%{buildroot}%{_datadir}/vim/vimfiles'
cp -vrp misc/vim/* '%{buildroot}%{_datadir}/vim/vimfiles'
find '%{buildroot}%{_datadir}/vim/vimfiles' \
    -type f -name 'README.*' -print -delete
%py_byte_compile %{python3} '%{buildroot}%{_datadir}/vim/vimfiles/gn-format.py'
install -t '%{buildroot}%{_emacs_sitestartdir}' -D -p -m 0644 misc/emacs/*.el
install -t '%{buildroot}%{_mandir}/man1' -D -m 0644 -p out/gn.1
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

out/gn_unittests
grep -E '^#define[[:blank:]]+LAST_COMMIT_POSITION_NUM[[:blank:]]+'\
'%{position}[[:blank:]]*' \
    'out/last_commit_position.h' >/dev/null
grep -E '^#define[[:blank:]]+LAST_COMMIT_POSITION[[:blank:]]+'\
'"%{position} \(%{shortcommit}\)"[[:blank:]]*' \
    'out/last_commit_position.h' >/dev/null
%files -f %{oreon_filedir}/main.list
%files -n gn-doc -f %{oreon_filedir}/gn-doc.list

%changelog

%autochangelog
