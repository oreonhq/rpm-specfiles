%global source0_hash 9b8afa4176bc1d8b18392779a5cb1ee8ae338a8a9c70bbe389d0511bae8eb208

%define		mainver		0.996
#%%define		betaver		pre3
%define		baserelease	17

%define set_javaver() \
%if 	0%{?fedora}%{?rhel} == %1 \
BuildRequires:	java-%2-openjdk-devel \
%if	%1 >= 42 \
BuildRequires:	javapackages-local-openjdk%2 \
%endif \
%endif \
%{nil}

Name:		mecab-java
Version:	%{mainver}
Release:	%{?betaver:0.}%{baserelease}%{?betaver:.%betaver}%{?dist}
Summary:	Java binding for MeCab

# SPDX confirmed
License:	BSD-3-Clause OR LGPL-2.1-or-later OR GPL-2.0-or-later
URL:		http://mecab.sourceforge.net/
Source0:	http://mecab.googlecode.com/files/%{name}-%{mainver}%{?betaver}.tar.gz

# This is not release number specific
BuildRequires:	make
BuildRequires:	gcc-c++
BuildRequires:	mecab-devel = %{version}
# java related macros
%set_javaver	45	25
%set_javaver	44	25
%set_javaver	43	21
%set_javaver	42	21

BuildRequires:	javapackages-tools
# %%check
BuildRequires:	mecab-jumandic
BuildRequires:	glibc-langpack-ja

Requires:	mecab = %{version}

ExclusiveArch:	%java_arches

%description
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{mainver}%{?betaver}
%{__sed} -i.opt -e 's|-O3||' Makefile

# ??? What are the following lines for?
# Disabling for now
: %{__sed} -i.test \
	-e '/test\.java/s|\$|-$|' Makefile

%build
# Failed with -j4 on Matt's mass build
%{__make} -j1 \
	CXX="g++ $RPM_OPT_FLAGS -fno-strict-aliasing" \
	JAVAC="%{javac} -encoding UTF8" \
	JAR=%{jar} \
	INCLUDE=/usr/lib/jvm/java/include

%install
#%%{__mkdir_p} $RPM_BUILD_ROOT%%{_libdir}
%{__mkdir_p} $RPM_BUILD_ROOT%{_libdir}/%{name}
%{__mkdir_p} $RPM_BUILD_ROOT%{_jnidir}

%{__install} -cm 644 MeCab.jar $RPM_BUILD_ROOT%{_jnidir}/
#%%{__install} -cm 755 libMeCab.so $RPM_BUILD_ROOT%%{_libdir}
%{__install} -cm 755 libMeCab.so $RPM_BUILD_ROOT%{_libdir}/%{name}/

%check
export JAVA=%{java}
LANG=ja_JP.utf8
%{__make} test || :

%files
%doc bindings.html
%doc AUTHORS COPYING BSD GPL LGPL

#%%{_libdir}/libMeCab.so
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/libMeCab.so
%{_jnidir}/MeCab.jar

%changelog
%autochangelog
