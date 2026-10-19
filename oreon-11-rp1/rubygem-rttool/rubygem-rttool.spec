%global source0_hash 4db7e95300d4b3ff7ad42e063a66497c45c19fa28f877fb8a9256ce9e211f460
%global	gem_name	rttool
Name:		rubygem-%{gem_name}
Version:	1.0.3.0
Release:        28%{?dist}
Summary:        Converter from RT into various formats
License:	Ruby OR GPL-2.0-only
URL:		https://github.com/genki/rttool
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires:	rubygem(racc)
Requires:	ruby(release)
Requires:	ruby(rubygems)
BuildArch:	noarch
Provides:	rubygem(%{gem_name}) = %{version}-%{release}
# oreon:deps
BuildRequires:  ruby(release)
BuildRequires:  rubygem(minitest)
BuildRequires:  rubygem(nkf)
BuildRequires:  rubygem(racc)
BuildRequires:  rubygem(rdtool)
BuildRequires:  rubygem(test-unit)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
RT is a simple and human-readable table format.
RTtool is a converter from RT into various formats.
RT can be incorporated into RD.

%package	doc
Summary:	Documentation for %{name}
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch
%description doc
Documentation for %{name}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n  %{gem_name}-%{version}
mv ../%{gem_name}-%{version}.gemspec .

# Encoding
for f in \
	rttool.*.*
do
	iconv -f EUC-JP -t UTF-8 -o $f{.utf,}
	touch -r $f{,.utf}
	mv $f{.utf,}
done

# shebang
sed -i \
	-e '\@#![ \t]*/usr/bin/ruby@d' \
	lib/rt/*.rb

%build

gem build %{gem_name}-%{version}.gemspec
%gem_install
%install
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
	%{buildroot}%{gem_dir}/
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
	%{buildroot}%{_bindir}/
find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

pushd .%{gem_instdir}
chmod 0755 bin/rt2
export RUBYOPT="-I$(pwd)/lib"
export PATH=$(pwd)/bin:$PATH
ruby -Ilib:. -e 'gem "minitest" ; Dir.glob("test/test*.rb").each {|f| require f}'
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-rttool-doc -f %{oreon_filedir}/rubygem-rttool-doc.list

%changelog

%autochangelog
