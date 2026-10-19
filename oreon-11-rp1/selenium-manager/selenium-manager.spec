%global source0_hash 67ff5dd5f1f5b6d6e6965b383ecc9ee9a112e5a255b81bde9deefc2f20ba3cf5
%global cargo_install_lib 0
Name:           selenium-manager
Version:        4.49.0
Release:        1%{?dist}
Summary:        Automated driver and browser management for Selenium
License:        %{shrink:
                Apache-2.0 AND
                BSD-3-Clause AND
                CDLA-Permissive-2.0 AND
                ISC AND
                MIT AND
                MPL-2.0 AND
                Unicode-3.0 AND
                Unicode-DFS-2016 AND
                bzip2-1.0.6 AND
                (0BSD OR MIT OR Apache-2.0) AND
                (Apache-2.0 OR BSL-1.0) AND
                (Apache-2.0 OR ISC OR MIT) AND
                (Apache-2.0 OR MIT) AND
                (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND
                (MIT OR Apache-2.0 OR Zlib) AND
                (Unlicense OR MIT)
                }
URL:            https://github.com/SeleniumHQ/selenium
Source0:        https://github.com/SeleniumHQ/selenium/archive/selenium-%{version}.tar.gz
Patch0:         0001-remove-unnecessary-dependencies.patch
Patch1:         0001-remove-unsupported-function.patch
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description
Selenium Manager is a command-line tool implemented in Rust
that provides automated driver and browser management for Selenium.

%prep
%autosetup -n selenium-selenium-%{version}/rust/ -N
%patch -P 0
cd src
%patch -P 1
cd ..
%oreon_vendor_cargo
%build

%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
%install
%cargo_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
