%global source0_hash effddbe6ac12b3065defae553a1fd3e3f43033bb7bc9f871744a2d122b3abd41

Name:           python-axolotl
Version:        0.2.3
Release:        %autorelease
Summary:        Python port of libaxolotl

License:        GPL-3.0-only
URL:            https://github.com/tgalal/python-axolotl
Source0:        %{url}/archive/%{version}/%{version}.tar.gz

# The protobuf dependency is too strict, this patch relaxes the requirement
# https://github.com/tgalal/python-axolotl/issues/44
Patch0:         python-axolotl-protobuf.patch
Patch1:         python-axolotl-remove-nose.patch

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
This is a ratcheting forward secrecy protocol
that works in synchronous and asynchronous messaging environments.}

%description %_description

%package -n python3-axolotl
Summary:        %{summary}

%description -n python3-axolotl %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files axolotl

%check
%tox

%files -n python3-axolotl -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
