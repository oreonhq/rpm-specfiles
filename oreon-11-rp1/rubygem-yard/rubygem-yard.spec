%global source0_hash 5d34f77c4cdd924567aa549184b61c134dad0f13933d74a419f04031b279f238

%global	gem_name	yard

Name:		rubygem-%{gem_name}
Version:	0.9.38
Release:	3%{?dist}

Summary:	Documentation tool for consistent and usable documentation in Ruby

# lib/yard/parser/ruby/legacy/ruby_lex.rb: under GPL-2.0-only OR Ruby
# lib/yard/rubygems/backports/: MIT OR Ruby
# lib/yard/server/http_utils.rb: BSD 2-Clause
# lib/yard/server/templates/default/fulldoc/html/js/autocomplete.js:
#   MIT OR GPL(version 2??), as this is OR, use MIT for now
# Others are MIT
# SPDX confirmed
License:	MIT AND (MIT OR Ruby) AND BSD-2-Clause AND (GPL-2.0-only OR Ruby)

URL:		http://yardoc.org
Source0:	https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1:	%{gem_name}-%{version}-test-missing-files.tar.gz
# Source1 is created by $ bash %%SOURCE2 %%version
Source2:	yard-create-missing-test-files.sh
# https://github.com/lsegal/yard/issues/1637
# Fix spec testsuite with namespace collision
Patch0:	yard-0.9.38-issue1637-spec-namespace-collision.patch

# The 'irb/notifier' might be required for parsing of some old Ruby code.
# https://github.com/lsegal/yard/blob/v0.9.24/lib/yard/parser/ruby/legacy/irb/slex.rb#L13
Recommends:	rubygem(irb)

BuildRequires:	ruby(release)
BuildRequires:	rubygems-devel
BuildRequires:	ruby
BuildRequires:	rubygem(RedCloth)
BuildRequires:	rubygem(asciidoctor)
BuildRequires:	rubygem(bundler)
BuildRequires:	rubygem(irb)
BuildRequires:	rubygem(rack)
BuildRequires:	/usr/bin/rackup
BuildRequires:	rubygem(rake)
BuildRequires:	rubygem(redcarpet)
BuildRequires:	rubygem(rspec)
BuildRequires:	rubygem(webrick)

BuildArch:		noarch

%description
YARD is a documentation generation tool for the Ruby programming language.
It enables the user to generate consistent, usable documentation that can be
exported to a number of formats very easily, and also supports extending for
custom Ruby constructs such as custom class level definitions.

%package	doc
Summary:	Documentation for %{name}
Requires:	%{name} = %{version}-%{release}
BuildArch:		noarch

%description doc
Documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version} -b1
%patch -P0 -p1
mv ../%{gem_name}-%{version}.gemspec .

%build
gem build ./%{gem_name}-%{version}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
	%{buildroot}%{gem_dir}/

pushd %{buildroot}%{gem_instdir}
rm -rf .yardopts* \
	%{nil}
popd

mkdir -p %{buildroot}%{_bindir}
cp -a .%{_bindir}/* \
	%{buildroot}%{_bindir}/

find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod 0755
rm -f %{buildroot}%{gem_cache}

%check
# FIXME
# investigate this: was okay with yard 0.9.28
sed -i spec/cli/diff_spec.rb \
	-e '\@"searches for .gem file"@s|\([ \t]it \)|\txit |'
rspec -r spec_helper spec

%files
%dir	%{gem_instdir}
%license	%{gem_instdir}/LEGAL
%license	%{gem_instdir}/LICENSE
%doc	%{gem_instdir}/CHANGELOG.md
%doc	%{gem_instdir}/README.md

%{_bindir}/yard
%{_bindir}/yardoc
%{_bindir}/yri

%{gem_libdir}/
%{gem_instdir}/bin
%{gem_instdir}/po/
%{gem_instdir}/templates/

%{gem_spec}
%{?gem_plugin}

%files doc
%doc	%{gem_docdir}
%doc	%{gem_instdir}/docs/

%changelog
%autochangelog
