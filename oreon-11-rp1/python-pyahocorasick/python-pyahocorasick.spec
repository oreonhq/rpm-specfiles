%global source0_hash 9d0f6bb522237ed7f111ed59c9e8baea7d1e75813587b6773babd43bda35db9f
Name:           python-pyahocorasick
Version:        2.3.1
Release:        1%{?dist}
Summary:        pyahocorasick is a fast and memory efficient library for exact or approximate multi-pattern string search.  With the __ahocorasick.Automaton__ class, you can find multiple key string occurrences at once in some input text.  You can use it as a plain dict-like Trie or convert a Trie to an automaton for efficient Aho-Corasick search. And pickle to disk for easy reuse of large automatons. Implemented in C and tested on Python 3.6+. Works on Linux, macOS and Windows. BSD-3-Cause license.
License:        ...
URL:            http://github.com/WojciechMula/pyahocorasick
Source0:        https://files.pythonhosted.org/packages/source/p/pyahocorasick/pyahocorasick-%{version}.tar.gz
Patch:          https://github.com/WojciechMula/pyahocorasick/pull/193.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-pyahocorasick = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-pyahocorasick
Summary:        pyahocorasick is a fast and memory efficient library for exact or approximate multi-pattern string search.  With the __ahocorasick.Automaton__ class, you can find multiple key string occurrences at once in some input text.  You can use it as a plain dict-like Trie or convert a Trie to an automaton for efficient Aho-Corasick search. And pickle to disk for easy reuse of large automatons. Implemented in C and tested on Python 3.6+. Works on Linux, macOS and Windows. BSD-3-Cause license.
%description -n python3-pyahocorasick

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir pyahocorasick-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pyahocorasick usr/lib/python3*/site-packages/pyahocorasick* usr/lib64/python3*/site-packages/pyahocorasick* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pyahocorasick* usr/lib64/python3*/site-packages/pyahocorasick* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-pyahocorasick -f %{oreon_filedir}/python3-pyahocorasick.list

%changelog

%autochangelog
