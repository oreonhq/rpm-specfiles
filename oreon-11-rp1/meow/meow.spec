%global source0_hash 00ba73786c02e7726f5143c95672d69adbc5595f4afb4841e6e33e5fc7b9c511
Name:		meow
Version:	2.1.5
Release:        1%{?dist}
Summary:        Print ASCII cats to your terminal
License:	%{shrink:
	MIT AND
	(Apache-2.0 OR MIT) AND
	(BSD-2-Clause OR Apache-2.0 OR MIT)
}
URL:		https://github.com/pixelsergey/meow
Source0:        https://github.com/pixelsergey/%{name}/archive/v%{version}/%{name}-v%{version}.tar.gz
ExcludeArch:	%{ix86}
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  help2man
BuildRequires:  rustc
# /oreon:deps
%description
This is a simple app to print ASCII cats directly to your terminal.
Run `meow` for a single cat, `meow -c <COUNT>` for more cats,
or `meow -l` if you think that you are literally the cat that will be printed.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup
%oreon_vendor_cargo
%build

%cargo_build
%{cargo_license} > LICENSE.dependencies
%{cargo_license_summary}
%install
install -p -D target/rpm/meow-cli %{buildroot}%{_bindir}/meow
install -d %{buildroot}%{_mandir}/man1
help2man --no-info --name='%{summary}' --version-string='%{version}' \
	--output=%{buildroot}%{_mandir}/man1/meow.1 \
	%{buildroot}%{_bindir}/meow
%oreon_autofiles main

%check

%cargo_test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
