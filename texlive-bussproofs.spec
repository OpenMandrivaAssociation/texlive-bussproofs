Name:		texlive-bussproofs
Version:	54080
Release:	1
Summary:	Proof trees in the style of the sequent calculus
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/bussproofs
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bussproofs.r54080.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bussproofs.doc.r54080.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package allows the construction of proof trees in the style
of the sequent calculus and many other proof systems. One novel
feature of the macros is they support the horizontal alignment
according to some centre point specified with the command
\fCenter. This is the style often used in sequent calculus
proofs. The package works in a Plain TeX document, as well as
in LaTeX; an exposition of the commands available is given in
the package file itself.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/bussproofs/bussproofs.sty
%doc %{_texmfdistdir}/doc/latex/bussproofs/BussGuide2.pdf
%doc %{_texmfdistdir}/doc/latex/bussproofs/BussGuide2.tex
%doc %{_texmfdistdir}/doc/latex/bussproofs/README.txt
%doc %{_texmfdistdir}/doc/latex/bussproofs/testbp2.pdf
%doc %{_texmfdistdir}/doc/latex/bussproofs/testbp2.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
