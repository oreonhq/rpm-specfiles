%global source0_hash b185cd8d81325f97c773582e50f1c5e047c2d8575b53d676469c9daf2a52f341
Name:           httpie
Version:        3.2.4
Release:        1%{?dist}
Summary:        A Curl-like tool for humans
License:        BSD-3-Clause
URL:            https://httpie.org/
Source0:        https://github.com/httpie/cli/archive/%{version}/cli-%{version}.tar.gz
Patch:          https://github.com/httpie/cli/pull/1643.patch
BuildArch:      noarch
%bcond_without tests
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-httpie = %{version}-%{release}
# /oreon:deps
%description
HTTPie is a CLI HTTP utility built out of frustration with existing tools. The
goal is to make CLI interaction with HTTP-based services as human-friendly as
possible.

HTTPie does so by providing an http command that allows for issuing arbitrary
HTTP requests using a simple and natural syntax and displaying colorized
responses.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n cli-%{version}

# Upstream pins werkzeug<2.1.0 to avoid a problem in httpbin that Fedora has patch for
# https://github.com/httpie/httpie/pull/1345
# we revert it to allow building with newer werkzeug
sed -i "/werkzeug<2.1.0/d" setup.cfg

%build

%pyproject_wheel
%install
%pyproject_install
mkdir -p %{buildroot}%{bash_completions_dir}
cp -a extras/httpie-completion.bash %{buildroot}%{bash_completions_dir}/http
ln -s ./http %{buildroot}%{bash_completions_dir}/https
mkdir -p %{buildroot}%{fish_completions_dir}/
cp -a extras/httpie-completion.fish %{buildroot}%{fish_completions_dir}/http.fish
ln -s ./http.fish %{buildroot}%{fish_completions_dir}/https.fish
mkdir -p %{buildroot}%{_mandir}/man1
cp -a extras/man/*.1 %{buildroot}%{_mandir}/man1/
%oreon_autofiles main

%check

%if %{with tests}
normalizer="not test_terminal_output_response_charset_detection and not test_terminal_output_request_charset_detection"
issue1530="not test_compress_form and not test_binary"
plugins="not test_plugins_installation and not test_plugin_installation_with_custom_config and not test_plugins_listing and not test_plugins_uninstall and not test_plugins_double_uninstall and not test_broken_plugins"
argparse="not (test_naked_invocation and args3)"
dr="not test_daemon_runner"
%pytest -v -k "$normalizer and $issue1530 and $plugins and $argparse and $dr"
%else
%pyproject_check_import
%endif
%files

%changelog

%autochangelog
