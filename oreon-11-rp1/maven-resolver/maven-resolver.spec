%global source0_hash dfead7be16788159b5f44b0b6842627f23901b48ea8cd26eade2083926d78ba6

%{lua:
if macros.orbs_chain_plan == nil and macros._without_bootstrap == nil then
  local spec
  local cmd = io.open("/proc/self/cmdline", "rb")
  if cmd then
    local data = cmd:read("*a") or ""
    cmd:close()
    local cur = ""
    local function take(arg)
      if string.sub(arg, -5) == ".spec" then spec = arg end
    end
    for i = 1, #data do
      local c = string.sub(data, i, i)
      if string.byte(c) == 0 then
        take(cur)
        cur = ""
      else
        cur = cur .. c
      end
    end
    take(cur)
  end
  local function trim(s)
    local a, b = 1, #s
    while a <= b do
      local c = string.sub(s, a, a)
      if c ~= " " and string.byte(c) ~= 9 then break end
      a = a + 1
    end
    while b >= a do
      local c = string.sub(s, b, b)
      if c ~= " " and string.byte(c) ~= 9 then break end
      b = b - 1
    end
    return string.sub(s, a, b)
  end
  local function miss(dep)
    local p = io.popen("dnf -q repoquery --latest-limit 1 --whatprovides '" .. dep .. "' 2>/dev/null")
    if not p then return true end
    local out = p:read("*a") or ""
    p:close()
    local i = 1
    while i <= #out do
      local b = string.byte(out, i)
      if b ~= 32 and b ~= 9 and b ~= 10 and b ~= 13 then return false end
      i = i + 1
    end
    return true
  end
  if spec then
    local f = io.open(spec, "r")
    if f then
      local depth, in_else, armed = 0, false, false
      for line in f:lines() do
        local s = trim(line)
        if not armed then
          if string.sub(s, 1, 3) == "%%if" and string.find(s, "{with bootstrap}", 1, true) then
            armed = true
            depth = 1
          end
        elseif string.sub(s, 1, 3) == "%%if" then
          depth = depth + 1
        elseif string.sub(s, 1, 6) == "%%endif" then
          depth = depth - 1
          if depth == 0 then break end
        elseif depth == 1 and string.sub(s, 1, 5) == "%%else" then
          in_else = true
        elseif in_else and depth == 1 and string.lower(string.sub(s, 1, 14)) == "buildrequires:" then
          local dep = trim(string.sub(s, 15))
          if dep ~= "" and string.sub(dep, 1, 1) ~= "%%" and miss(dep) then
            rpm.define("_with_bootstrap 1")
            break
          end
        end
      end
      f:close()
    end
  end
end
}
%bcond_with bootstrap
Name:           maven-resolver
Epoch:          1
Version:        1.9.27
Release:        %autorelease
Summary:        Apache Maven Artifact Resolver library
License:        Apache-2.0
URL:            https://maven.apache.org/resolver/
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        https://archive.apache.org/dist/maven/resolver/maven-resolver-%{version}-source-release.zip

Patch:          0001-Remove-use-of-deprecated-SHA-1-and-MD5-algorithms.patch
Patch:          0002-Make-I-O-errors-during-test-cleanup-non-fatal.patch

%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(com.google.inject:guice)
BuildRequires:  mvn(commons-codec:commons-codec)
BuildRequires:  mvn(javax.inject:javax.inject)
BuildRequires:  mvn(javax.servlet:javax.servlet-api)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.httpcomponents:httpclient)
BuildRequires:  mvn(org.apache.httpcomponents:httpcore)
BuildRequires:  mvn(org.apache.maven.wagon:wagon-provider-api)
BuildRequires:  mvn(org.apache.maven:maven-model-builder)
BuildRequires:  mvn(org.apache.maven:maven-parent:pom:)
BuildRequires:  mvn(org.apache.maven:maven-resolver-provider)
BuildRequires:  mvn(org.codehaus.plexus:plexus-classworlds)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)
BuildRequires:  mvn(org.codehaus.plexus:plexus-xml)
BuildRequires:  mvn(org.eclipse.sisu:org.eclipse.sisu.inject)
BuildRequires:  mvn(org.eclipse.sisu:org.eclipse.sisu.plexus)
BuildRequires:  mvn(org.eclipse.sisu:sisu-maven-plugin)
BuildRequires:  mvn(org.hamcrest:hamcrest)
BuildRequires:  mvn(org.hamcrest:hamcrest-core)
BuildRequires:  mvn(org.mockito:mockito-core)
BuildRequires:  mvn(org.slf4j:jcl-over-slf4j)
BuildRequires:  mvn(org.slf4j:slf4j-api)
BuildRequires:  mvn(org.slf4j:slf4j-simple)
%endif
# TODO Remove in Fedora 46
Obsoletes:      %{name}-javadoc < 1:1.9.22-10
Provides:       maven-resolver-api = %{epoch}:%{version}-%{release}
Provides:       maven-resolver-connector-basic = %{epoch}:%{version}-%{release}
Provides:       maven-resolver-impl = %{epoch}:%{version}-%{release}
Provides:       maven-resolver-spi = %{epoch}:%{version}-%{release}
Provides:       maven-resolver-transport-classpath = %{epoch}:%{version}-%{release}
Provides:       maven-resolver-transport-file = %{epoch}:%{version}-%{release}
Provides:       maven-resolver-transport-http = %{epoch}:%{version}-%{release}
Provides:       maven-resolver-transport-wagon = %{epoch}:%{version}-%{release}
Provides:       maven-resolver-util = %{epoch}:%{version}-%{release}

%description
Apache Maven Artifact Resolver is a library for working with artifact
repositories and dependency resolution. Maven Artifact Resolver deals with the
specification of local repository, remote repository, developer workspaces,
artifact transports and artifact resolution.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1

# Skip tests that equire internet connection
rm maven-resolver-supplier/src/test/java/org/eclipse/aether/supplier/RepositorySystemSupplierTest.java
rm maven-resolver-transport-http/src/test/java/org/eclipse/aether/transport/http/{HttpServer,HttpTransporterTest}.java
%pom_remove_dep org.eclipse.jetty: maven-resolver-transport-http

%pom_remove_plugin -r :bnd-maven-plugin
%pom_remove_plugin -r org.codehaus.mojo:animal-sniffer-maven-plugin
%pom_remove_plugin -r :japicmp-maven-plugin
%pom_remove_plugin -r :maven-enforcer-plugin

%pom_disable_module maven-resolver-demos
%pom_disable_module maven-resolver-named-locks-hazelcast
%pom_disable_module maven-resolver-named-locks-redisson
%pom_disable_module maven-resolver-transport-classpath
%mvn_package :maven-resolver-test-util __noinstall

# generate OSGi manifests
for pom in $(find -mindepth 2 -name pom.xml) ; do
  %pom_add_plugin "org.apache.felix:maven-bundle-plugin" $pom \
  "<configuration>
    <instructions>
      <Bundle-SymbolicName>\${project.groupId}$(sed 's:./maven-resolver::;s:/pom.xml::;s:-:.:g' <<< $pom)</Bundle-SymbolicName>
      <Export-Package>!org.eclipse.aether.internal*,org.eclipse.aether*</Export-Package>
      <_nouses>true</_nouses>
    </instructions>
  </configuration>
  <executions>
    <execution>
      <id>create-manifest</id>
      <phase>process-classes</phase>
      <goals><goal>manifest</goal></goals>
    </execution>
  </executions>"
done
%pom_add_plugin "org.apache.maven.plugins:maven-jar-plugin" pom.xml \
"<configuration>
  <archive>
    <manifestFile>\${project.build.outputDirectory}/META-INF/MANIFEST.MF</manifestFile>
  </archive>
</configuration>"

%mvn_alias 'org.apache.maven.resolver:maven-resolver{*}' 'org.eclipse.aether:aether@1'
%mvn_alias 'org.apache.maven.resolver:maven-resolver-transport-wagon' 'org.eclipse.aether:aether-connector-wagon'
%mvn_file ':maven-resolver{*}' %{name}/maven-resolver@1 aether/aether@1

%build
%mvn_build -j

%install
%mvn_install

%files -f .mfiles
%license LICENSE NOTICE

%changelog
%autochangelog
