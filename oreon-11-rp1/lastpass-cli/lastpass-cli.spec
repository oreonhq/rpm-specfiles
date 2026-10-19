%global source0_hash 9989ef0650db18bc3f80ba52964202b778abda0548f95dcd321e9c7c39a1a24e
Name:           lastpass-cli
Version:        1.6.1
Release:        1%{?dist}
Summary:        Command line interface to LastPass.com
License:        GPL-2.0-or-later WITH cryptsetup-OpenSSL-exception AND OpenSSL
URL:            https://github.com/LastPass/lastpass-cli
Source0:        https://github.com/LastPass/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch:          lastpass-cli-1.3.1-remove_reallocarray.patch
Requires:       pinentry
Requires:       xclip
# oreon:deps
BuildRequires:  asciidoc
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(openssl)
# /oreon:deps
%description
A command line interface to LastPass.com.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake
%cmake_build --target lpass doc-man doc-html
%install
export DESTDIR=%{buildroot}
%cmake_build --target install-doc
%cmake_install
install -Dpm0644 contrib/lpass_bash_completion -t \
    %{buildroot}%{bash_completions_dir}/lpass-completion.bash
install -Dpm0644 contrib/completions-lpass.fish -t \
    %{buildroot}%{fish_completions_dir}/lpass.fish
install -Dpm0644 contrib/lpass_zsh_completion -t \
    %{buildroot}%{zsh_completions_dir}/_lpass
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
