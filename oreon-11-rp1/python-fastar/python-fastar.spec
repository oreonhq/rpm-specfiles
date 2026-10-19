%global source0_hash 1da58f764b88694485134b4bfdc1a9ebdb1dbb8f4fc82018742982593e63b2ee
Name:           python-fastar
Version:        0.12.0
Release:        1%{?dist}
Summary:        High-level bindings for the Rust tar crate
License:        MIT
URL:            https://github.com/DoctorJohn/fastar
Source0:        https://github.com/DoctorJohn/fastar/archive/v%{version}/fastar-%{version}.tar.gz
Patch:          fastar-0.9.0-allow-pyo3-0.27.patch
%global common_description %{expand:
The fastar library wraps the Rust tar, flate2, and zstd crates, providing a
high-performance way to work with compressed and uncompressed tar archives in
Python.}
# oreon:deps
BuildRequires:  cargo-rpm-macros
BuildRequires:  python3dist(psutil)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(typing-extensions)
BuildRequires:  tomcli
# /oreon:deps
%description %{common_description}

%package -n     python3-fastar
Summary:        High-level bindings for the Rust tar crate
License:        %{shrink:
                MIT AND
                (0BSD OR MIT OR Apache-2.0) AND
                (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND
                (MIT OR Apache-2.0) AND
                (MIT OR Zlib OR Apache-2.0)
                }
%description -n python3-fastar %{common_description}

%prep
%oreon_prep
%build -p

%cargo_license_summary
%{cargo_license} > LICENSE.dependencies
%install
%pyproject_install
%oreon_autofiles python3-fastar usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

k="${k-}${k+ and }not test_close_closes_archive"
k="${k-}${k+ and }not test_context_manager_closes_archive"
k="${k-}${k+ and }not test_unpack_preserves_file_modification_time_only_if_option_is_true"
ignore="${ignore-} --ignore=tests/benchmarks/"
%pytest -k "${k-}" ${ignore} -v
%files -f %{oreon_filedir}/main.list
%files -n python3-fastar -f %{oreon_filedir}/python3-fastar.list

%changelog

%autochangelog
