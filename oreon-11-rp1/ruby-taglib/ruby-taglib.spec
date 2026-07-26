%global source0_hash 0f69a72cdcf030453185c9b87297df9788e956bf63e1f3075f74e7625e9be910

Name:		ruby-taglib
Version:	1.1
Release:	36%{?dist}
Summary:	Ruby library wrapping the Taglib library

# SPDX confirmed
License:	MIT-open-group
URL:		http://www.hakubi.us/ruby-taglib/
Source0:	http://www.hakubi.us/ruby-taglib/%{name}-%{version}.tar.bz2
# Patch from debian
Patch0:		ruby-taglib-1.1-debian-10_so-name.dpatch
Patch1:		ruby-taglib-1.1-debian-20_tag-undefined.dpatch
# Ruby 2.2 finaly removed Config in favor of RbConfig.
Patch2:		ruby-taglib-1.1-ruby22-fix.patch

BuildArch:	noarch

Requires:	ruby(release)
BuildRequires:	ruby(release)

BuildRequires:	ruby-devel
Requires:	taglib
Provides:	ruby(taglib) = %{version}-%{release}

%description
ruby-taglib is a simple dl-based wrapper of
Taglib's C library.  It's short and sweet, because the C API is written by
someone who knows how to use OO programming, and Ruby with dl just
makes it all too easy to wrap such a library.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1 -b .soname
%patch -P1 -p1 -b .warn
%patch -P2 -p1 -b .ruby22

%build
ruby setup.rb config \
	--prefix=%{_prefix} \
	--siterubyver=%{ruby_vendorlibdir}
ruby setup.rb setup

%install
%{__rm} -rf $RPM_BUILD_ROOT

ruby setup.rb install \
	--prefix=$RPM_BUILD_ROOT

%files
%doc README

%{ruby_vendorlibdir}/taglib.rb

%changelog
%autochangelog
