%global source0_hash fee5a30823aa24153933850486c99b09c290669f24cf7fc34c051d765a8b817d

%global commit      5a1c8d83ba1514ca8d045ba80403f93772fb371a
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global date        2020704

%bcond_without  tests

Name:           the_silver_searcher
Version:        2.2.0^%{date}.%{shortcommit}
Release:        15%{?dist}
Summary:        Super-fast text searching tool (ag)
# The bundled copy of src/uthash.h is BSD-1-Clause, but we remove that in
# %%prep so this package is only Apache-2.0.
License:        Apache-2.0
URL:            https://github.com/ggreer/the_silver_searcher
Source:         %{url}/archive/%{commit}/%{name}-%{commit}.tar.gz

# https://github.com/ggreer/the_silver_searcher/pull/1145
Patch:          0001-update-zsh-completion-for-new-options.patch
# https://github.com/ggreer/the_silver_searcher/pull/1410
Patch:          0002-Install-shell-completion-files-to-correct-locations.patch
# https://github.com/ggreer/the_silver_searcher/pull/1540
Patch:          0003-bash-completion-port-to-v2-API.patch
# https://packages.debian.org/source/sid/silversearcher-ag
# http://deb.debian.org/debian/pool/main/s/silversearcher-ag/silversearcher-ag_2.2.0+git20200805-1.2.debian.tar.xz
Patch:          enable_pcre2_support.patch

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  pcre2-devel
BuildRequires:  xz-devel
BuildRequires:  zlib-devel
BuildRequires:  uthash-devel
%if %{with tests}
BuildRequires:  python3-cram
BuildRequires:  git-core
%endif

Provides:       ag

%description
The Silver Searcher is a code searching tool similar to ack,
with a focus on speed.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{commit} -p 1

# https://github.com/ggreer/the_silver_searcher/issues/1411
rm src/uthash.h
sed -e '/ag_SOURCES/ s/ src\/uthash.h//' -i Makefile.am

%build
aclocal
autoconf
autoheader
automake --add-missing
%configure --disable-silent-rules
%make_build

%install
%make_install

%if %{with tests}
%check
make test
%endif

%files
%license LICENSE
%doc README.md
%{_bindir}/ag
%{_mandir}/man1/ag.1*
%{_datadir}/bash-completion/completions/ag
%{_datadir}/zsh/site-functions/_ag

%changelog
%autochangelog
