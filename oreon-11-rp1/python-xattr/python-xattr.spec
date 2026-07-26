%global source0_hash 9fc6197e1810c9e9cb4a7199a63847b199ba5ed7c90c5fdb81cbf5b8f260f910

Name:           python-xattr
Version:        1.3.0
Release:        %autorelease
Summary:        Python wrapper for extended filesystem attributes

License:        MIT
URL:            https://github.com/xattr/xattr
Source:         %{url}/archive/v%{version}/v%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  python3-devel
# Test dependencies
BuildRequires:  pytest

# Not needed for multilib
ExcludeArch: %{ix86}

%global _description %{expand:
Extended attributes extend the basic attributes of files and directories in the
file system. They are stored as name:data pairs associated with file system
objects (files, directories, symlinks, etc).
}

%description %_description

%package -n python3-xattr
Summary:        %{summary}

%description -n python3-xattr %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n xattr-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files xattr

%check
# in Copr, skip tests that fail with OSError: [Errno 95] Operation not supported
%pytest %{?copr_projectname:-k 'not (test_attr_fs_encoding_ascii or test_attr_fs_encoding_unicode or test_update)'}

%files -n python3-xattr -f %{pyproject_files}
%doc CHANGES.txt README.rst
%license LICENSE.txt
%{_bindir}/xattr

%changelog
%autochangelog
