%global source0_hash fee5a30823aa24153933850486c99b09c290669f24cf7fc34c051d765a8b817d
%global commit      5a1c8d83ba1514ca8d045ba80403f93772fb371a
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global date        2020704
%bcond_without  tests
Name:           the_silver_searcher
Version:        2.2.0^%{date}.%{shortcommit}
Release:        1%{?dist}
Summary:        Super-fast text searching tool (ag)
License:        Apache-2.0
URL:            https://github.com/ggreer/the_silver_searcher
Source0:        https://github.com/ggreer/%{name}/archive/%{commit}/%{name}-%{commit}.tar.gz
Patch:          0001-update-zsh-completion-for-new-options.patch
Patch:          0002-Install-shell-completion-files-to-correct-locations.patch
Patch:          0003-bash-completion-port-to-v2-API.patch
Patch:          enable_pcre2_support.patch
%if %{with tests}
%endif
Provides:       ag
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  git-core
BuildRequires:  make
BuildRequires:  pcre2-devel
BuildRequires:  python3-cram
BuildRequires:  uthash-devel
BuildRequires:  xz-devel
BuildRequires:  zlib-devel
# /oreon:deps
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
%oreon_autofiles main
%if %{with tests}
%check

make test
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
