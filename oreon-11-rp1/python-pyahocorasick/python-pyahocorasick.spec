%global source0_hash none

Name:           python-pyahocorasick
Version:        2.3.1
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        pyahocorasick is a fast and memory efficient library for exact or approximate multi-pattern string search.  With the __ahocorasick.Automaton__ class, you can find multiple key string occurrences at once in some input text.  You can use it as a plain dict-like Trie or convert a Trie to an automaton for efficient Aho-Corasick search. And pickle to disk for easy reuse of large automatons. Implemented in C and tested on Python 3.6+. Works on Linux, macOS and Windows. BSD-3-Cause license.

# No license information obtained, it's up to the packager to fill it in
License:        ...
URL:            http://github.com/WojciechMula/pyahocorasick
Source:         %{pypi_source pyahocorasick}

BuildRequires:  python3-devel
BuildRequires:  gcc


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'pyahocorasick' generated automatically by pyp2spec.}

Patch:          https://github.com/WojciechMula/pyahocorasick/pull/193.patch

%description %_description

%package -n     python3-pyahocorasick
Summary:        %{summary}

%description -n python3-pyahocorasick %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-pyahocorasick testing


%prep
%autosetup -p1 -n pyahocorasick-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x testing


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-pyahocorasick -f %{pyproject_files}

%changelog
%autochangelog
